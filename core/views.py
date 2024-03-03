from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.template import loader

def menu(request):
    return render(request, 'menu.html')

def home(request):
    return render(request, 'home.html')


@login_required
def task(request):
    return render(request, 'task.html')


@login_required
def sair(request):
    logout(request)
    return redirect('home')



def sigup(request):

    if str(request.method) == 'GET':
        return render(request, 'sigup.html',
                      {'form': UserCreationForm})
    else:
        if str(request.POST['password1']) == str(request.POST['password2']):
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save

                login(request, user)
                return redirect('task')
            except:
                messages.error(request, 'Usuário já Existe!')
                return render(request, 'sigup.html',
                              {'form': UserCreationForm })
        
        messages.error(request, 'Senhas estão Diferentes !')
        return render(request, 'sigup.html',
                        {'form': UserCreationForm})



def sigin(request):

    if request.method == 'GET':
        return render(request,'sigin.html',
                      {'form': UserCreationForm})
    else:
        user = authenticate(request,    
                            username=request.POST['username'], 
                            password=request.POST['password'])
        
        if user is None:
            messages.error(request, 'Usuário ou Senha Incorretos')
            return render(request, 'sigin.html', 
                          {'form': AuthenticationForm})
        else:
            login(request, user)
            return redirect('task')

def error404(request, ex):
    template= loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template= loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
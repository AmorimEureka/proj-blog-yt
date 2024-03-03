from django.urls import path
from django.conf.urls import handler404, handler500

from core import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('home/', views.home, name='home'),
    path('sigup/', views.sigup, name='sigup'),
    path('sigin/', views.sigin, name='sigin'),
    path('task/', views.task, name='task'),
    path('sair/', views.sair, name='sair'),

]

handler404 = views.error404
handler500 = views.error500

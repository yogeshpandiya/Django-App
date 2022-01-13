from django.urls import path

from . import views

urlpatterns = [
    path('Home', views.index, name='index'),
    path('', views.index, name='index'),
    path('Login', views.Login, name='Login'),
    path('SignUp', views.SignUp, name='SignUp'),
    path('Submit', views.Submit, name='Submit'),
    path('ULogin', views.ULogin, name='Login'),
    path('user', views.user, name='user'),
    path('calc', views.calc, name='calc'),
]

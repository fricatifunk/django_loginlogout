from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',views.home,name='home'),
    path('registro/',views.registro,name='registro'),
    path('profile/',views.profile,name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='paginas/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='paginas/logout.html'), name="logout"),

    
    
    ]

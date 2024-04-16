from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('register-form/', views.register_form, name='register_form'),
    path('login-form/', views.login_form, name='login_form'),
]

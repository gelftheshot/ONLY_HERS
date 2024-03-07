from django.urls import path
from . import views

app_name = 'userauths'

urlpatterns = [
    path('signup/', views.user_register, name='signup-page'),
    path('login/', views.user_login, name='login-page'),
    path('logout/', views.user_logout, name='logout-page')
]
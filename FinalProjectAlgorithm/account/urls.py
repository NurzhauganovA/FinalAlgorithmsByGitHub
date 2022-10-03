from django.urls import path
from . import views


urlpatterns = [
    path('login', views.AccountLogin, name='account_login'),
    path('register', views.AccountRegister, name='account_register'),
    path('logout', views.AccountLogout, name='account_logout'),
    path('profile', views.ProfileView, name='user_profile')
]

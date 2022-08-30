from django.urls import path
from . import views

app_name = 'authentication'
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_user, name='login'),
    path('success', views.login_user, name='success'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('register_user', views.register_user, name='register_user')
]

from django.urls import path
from . import views

urlpatterns = [
    path('login', views.account, name='account'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout')
]

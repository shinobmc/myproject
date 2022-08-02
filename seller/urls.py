from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('test', views.test, name='name'),
    path('login', views.login, name='login'),
    path('table', views.table, name='table')
]
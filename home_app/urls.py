from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('index/', views.index_page, name='index'),
    
   
    
]
from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', views.Tabmenu.as_view(), name='tab_menu'),
]



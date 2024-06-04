from django.urls import path
from . import views
from django import template

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('medicine/<int:pk>/', views.medicine_detail, name='medicine_detail'),
    path('medicine/new/', views.medicine_create, name='medicine_create'),
    path('medicine/<int:pk>/edit/', views.medicine_edit, name='medicine_edit'),
    path('medicine/<int:pk>/delete/', views.medicine_delete, name='medicine_delete'),
]
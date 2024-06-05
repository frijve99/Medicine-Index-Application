from django.urls import path
from . import views
from django import template
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('medicine/<int:pk>/', views.medicineDetails, name='medicineDetails'),
    path('medicine/new/', views.medicine_create, name='medicine_create'),
    path('medicine/<int:pk>/edit/', views.medicine_edit, name='medicine_edit'),
    path('medicine/<int:pk>/delete/', views.medicine_delete, name='medicine_delete'),
    path('medicine/signin' , views.signin , name='signin'),
    path('medicine/createAdmin' , views.createAdmin , name='createAdmin'),
    path('medicine/logout' , views.logout , name='logout'),
    path('medicine/viewAdmins' , views.viewAdmins , name='viewAdmins'),
    path('medicine/viewMedicines' , views.viewMedicines , name='viewMedicines'),
    path('medicine/addMedicines' , views.addMedicines , name='addMedicines')
    
]
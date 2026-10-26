from django.urls import path
from . import views

urlpatterns = [
    path('listusers/', views.listusers, name='listusers'),
    path('userhome/', views.userhome, name='userhome'),
    path('additems/', views.additems, name='additems'),
    path('adduser_success/', views.additems_success, name='additems_success'),
]    
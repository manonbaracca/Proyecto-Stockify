from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='dashboard-index'), 
    path('staff/', views.staff, name='dashboard-staff'), 
    path('producto/', views.producto, name='dashboard-producto'), 
    path('pedido/', views.pedido, name='dashboard-pedido'), 
]





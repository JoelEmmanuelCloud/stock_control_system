from django.urls import path
from .views import material_list, home, material_quantity_chart, dashboard

urlpatterns = [
    path('', home, name='home'),
    path('materials/', material_list, name='material_list'),
    path('dashboard/', dashboard, name='dashboard'),
]

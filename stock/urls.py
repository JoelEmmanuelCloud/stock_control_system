from django.urls import path
from .views import material_list, home, material_quantity_chart

urlpatterns = [
    path('', home, name='home'),
    path('k/', material_list, name='material_list'),
    path('dashboard/', material_quantity_chart, name='material_quantity_chart'),
]

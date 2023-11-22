from django.urls import path
from .views import material_list

urlpatterns = [
    path('materials/', material_list, name='material_list'),
]

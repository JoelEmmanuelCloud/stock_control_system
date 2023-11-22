from django.urls import path
from .views import material_list, home

urlpatterns = [
    path('k/', material_list, name='material_list'),
    path('', home, name='home'),
]

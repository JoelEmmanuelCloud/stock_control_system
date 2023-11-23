from django.urls import path
from .views import material_list, home, dashboard, ContactAdminView, AboutSystemView

urlpatterns = [
    path('', home, name='home'),
    path('materials/', material_list, name='material_list'),
    path('dashboard/', dashboard, name='dashboard'),
    path('contact-admin/', ContactAdminView, name='contact_admin'),
    path('about-system/', AboutSystemView, name='about_system'),
]

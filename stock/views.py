from django.shortcuts import render
from chartjs.views.lines import BaseLineChartView
from .models import Material

def material_list(request):
    materials = Material.objects.all()
    return render(request, 'stock/material_list.html', {'materials': materials})

def home(request):
    return render(request, 'stock/home.html')

class MaterialQuantityChartView(BaseLineChartView):
    def get_labels(self):
        return [material.name for material in Material.objects.all()]

    def get_data(self):
        return [material.quantity for material in Material.objects.all()]

    def get_colors(self):
        return [{'border_color': 'rgba(75, 192, 192, 1)', 'background_color': 'rgba(75, 192, 192, 0.2)'}]

    def get_datasets(self, **kwargs):
        data = self.get_data()
        return [{'data': data, **kwargs}]

material_quantity_chart = MaterialQuantityChartView.as_view()
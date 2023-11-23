from django.shortcuts import render
from .models import Material
from chartjs.views.lines import BaseLineChartView

def ContactAdminView(request):
    return render(request, 'stock/contact_admin.html')


def AboutSystemView(request):
    return render(request, 'stock/about_system.html')

def home(request):
    return render(request, 'stock/home.html')

def material_list(request):
    materials = Material.objects.all()
    return render(request, 'stock/material_list.html', {'materials': materials})

def dashboard(request):
    materials = Material.objects.all()
    labels = [material.name for material in materials]
    data = [material.quantity for material in materials]

    chart_data = {
        "labels": labels,
        "datasets": [{
            "data": data,
            "backgroundColor": "rgba(75, 192, 192, 0.2)",
            "borderColor": "rgba(75, 192, 192, 1)",
            "borderWidth": 1,
            "label": 'Material Quantities',
        }],
    }

    return render(request, 'stock/dashboard.html', {'chart_data': chart_data, 'materials': materials})

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

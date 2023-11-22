# stock/models.py
from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=50, null=True, blank=True)
    unit = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

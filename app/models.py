from django.db import models

class Pizza(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    activo = models.BooleanField(default=True)

class Ingrediente(models.Model):
    CATEGORIA_CHOICES = [
        ('Basico', 'Básico'),
        ('Premium', 'Premium'),
    ]
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES)

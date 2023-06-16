from django.contrib import admin
from .models import *



@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'activo')

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')
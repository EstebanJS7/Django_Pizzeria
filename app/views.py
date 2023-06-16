

# Create your views here.
from django.shortcuts import render
from app.models import Pizza, Ingrediente

def prueba_view(request):
    pizzas = Pizza.objects.all()
    ingredientes = Ingrediente.objects.all()
    context = {
        'pizzas':  pizzas,
        'ingredientes': ingredientes
    }

    return render(request, 'test.html', context)
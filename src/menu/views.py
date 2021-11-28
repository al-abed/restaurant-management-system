from django.shortcuts import render
from .models import Food

# Create your views here.

#CRUD - create, retrieve, update, delete

#LIST all the food items

def food_list_view(request):
    food_objects = Food.objects.all()
    
    context = {
        'food_objects': food_objects
    }

    return render(request, "menu/menu.html", context)
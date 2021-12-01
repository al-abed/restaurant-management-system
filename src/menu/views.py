from django.shortcuts import render
from django.http import JsonResponse
import json
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

def updateItem(request):
    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']

    print('ProductId: ', productId)
    print('Action: ', action)
    return JsonResponse('Item was added', safe = False)
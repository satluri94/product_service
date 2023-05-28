from django.shortcuts import render
import requests


from . import serializers
from rest_framework import viewsets
from .serializers import CartItemSerializer
from .models import CartItem
from .models import User
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.conf import settings
from django.contrib.auth import authenticate
import json
from rest_framework import permissions
from rest_framework import views
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
def get_trains(request):
    with open(settings.STATICFILES_DIRS[0] + '/trains.json', 'r') as f:
        data = json.load(f)
    return JsonResponse(data, safe=False)      

def get_stations(request):
    with open(settings.STATICFILES_DIRS[0] + '/stations.json', 'r') as f:
        data = json.load(f)
    return JsonResponse(data, safe=False)
    
def get_restaurantsForDropdown(request):
    with open(settings.STATICFILES_DIRS[0] + '/restaurantsForDropDown.json', 'r') as f:
        data = json.load(f)
    return JsonResponse(data, safe=False)
    
def get_restaurants(request):
    with open(settings.STATICFILES_DIRS[0] + '/restaurants.json', 'r') as f:
        data = json.load(f)
    return JsonResponse(data, safe=False)
    
def get_foodItems(request):
    with open(settings.STATICFILES_DIRS[0] + '/foodItems.json', 'r') as f:
        data = json.load(f)
    return JsonResponse(data, safe=False)
    
    
class CartItemView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    

@api_view(['POST'])
def addCartItem(request):
    if request.method == 'POST':
        new_cart_data = JSONParser().parse(request)
        food_title = new_cart_data['title']
        food_price = new_cart_data['price']
        if food_title is not None and food_price is not None:
            items = CartItem.objects.all()
            item = items.filter(title=food_title)
            if(item is not None):
                serializer = None
                serializer = CartItemSerializer(data=new_cart_data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({'message': 'Item already exists!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'message': 'One of the fields is empty!'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
def placeOrder(request):
    if request.method == 'POST':
        items = CartItem.objects.all()
        if(items is not None):
            cartList = None
            cartList = list(items.values())
            print(cartList)
            headers_data = {'Content-Type': 'application/json', 'Accept':'application/json'}
            response = requests.post('http://127.0.0.1:8002/api/admdash/orders/place/', json=cartList, headers=headers_data)
            resp = (response.content).decode('utf-8')
            return JsonResponse(resp, safe=False, status=response.status_code)
        else:
            return JsonResponse({'message': 'Cart is empty!'}, status=status.HTTP_204_NO_CONTENT)

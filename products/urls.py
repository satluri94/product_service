from django.urls import path
from products.views import CartItemView
from . import views


urlpatterns = [
    path('trains/', views.get_trains, name='get_trains'),
    path('stations/', views.get_stations, name='get_stations'),
    path('restaurantsForDropDown/', views.get_restaurantsForDropdown, name='get_restaurantsForDropdown'),
    path('restaurants/', views.get_restaurants, name='get_restaurants'),
    path('foodItems/', views.get_foodItems, name='get_foodItems'),
    path('cartItem/add/', views.addCartItem, name='add_cart_items'),
    path('cartItems/', CartItemView.as_view(), name='get_cartItems'),
    path('placeOrder/', views.placeOrder, name='place_order')
]

from django.urls import path 
from .views import *

urlpatterns = [
     path('cart' , CartView.as_view()),
     path('onlycart' , Cart_for.as_view()),
     path('cartitem' , Cart_for_item.as_view()),
     path('cart-fetch' , Cart_fetch.as_view()),
     path('cart-item-fetch/<int:pk>' , Cart_item_fetch_singular.as_view()),
     path('cart-item-fetch' , Cart_item_fetch_plural.as_view()),
]
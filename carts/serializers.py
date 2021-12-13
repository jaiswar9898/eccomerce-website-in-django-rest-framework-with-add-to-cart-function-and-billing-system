from rest_framework import serializers
from carts.models import Cart, CartItems
from vapp.serializers import * 

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__' 

class CartItemsSerializers_fetch(serializers.ModelSerializer):
    cart = CartSerializers()
    product = ProductSerializer()
    class Meta:
        model = CartItems
        fields = '__all__' 

class CartItemsSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = CartItems
        fields = '__all__' 
        


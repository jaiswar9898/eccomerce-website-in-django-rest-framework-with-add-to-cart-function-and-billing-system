from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny, IsAuthenticated
from carts.models import Cart,CartItems
from vapp.models import Product
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.http import HttpResponse
# Create your views here.
class CartView(APIView):
    # permission_classes = [AllowAny]
    def get(self , request):
#         
        queryset = CartItems.objects.all()
        serializer = CartItemsSerializers_fetch(queryset, many = True)
        return Response(serializer.data)
    
    

class Cart_for(APIView):
    serializer_class = CartSerializers
    def post(self, request, format=None):
        print(request.data)  #request.data will create form 
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
        


class Cart_for_item(APIView):
    serializer_class = CartItemsSerializers
    def post(self, request, format=None):
        print(request.data)  #request.data will create form 
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class Cart_fetch(APIView):
    serializer_class = CartSerializers
    def get(self , request):
#         
        queryset = Cart.objects.all()
        serializer = CartSerializers(queryset, many = True)
        return Response(serializer.data)

# This will fetch the all id of Cartitem 
class Cart_item_fetch_plural(APIView):
    serializer_class = CartItemsSerializers
    def get(self , request):
        
        queryset = CartItems.objects.all()
        serializer = CartItemsSerializers(queryset, many = True)
        return Response(serializer.data)



# This will fetch id one by one with help of pk 
class Cart_item_fetch_singular(APIView):
    serializer_class = CartItemsSerializers

    def get_object(self, pk):
        try:
            return CartItems.objects.get(pk=pk)
        except CartItems.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        
        serializer = self.serializer_class(self.get_object(pk)) 
        serialized_data = serializer.data
        print(serialized_data)

        return Response(serialized_data, status=status.HTTP_200_OK)


    def delete(self, request, pk, format=None):
        checklist_item = self.get_object(pk)
        checklist_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        device = self.get_object(pk)
        serializer = CartItemsSerializers(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

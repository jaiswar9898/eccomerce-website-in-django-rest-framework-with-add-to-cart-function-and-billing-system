from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
from .serializers import *
from .models import * 
from rest_framework.views import APIView, Response
from rest_framework import status
from .serializers import *
from django.http import HttpResponse
from django.http import Http404
from rest_framework import status, generics

def index(request):
        product_objects = Product.objects.all()
        template_name = 'home.html'
        return render(request,template_name,{'product_objects': product_objects})

def detail(request,id):
    product_objects = Product.objects.get(id=id)
    return render(request,'detail.html',{'product_objects':product_objects})

class ProductView(APIView):

    serializer_class = ProductSerializer

#This is for plural 
    def get(self,request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):

        print(request.data)  #request.data will create form 
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# This is for singular 
class ProductView_singular(APIView):

    serializer_class = ProductSerializer
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        
        serializer = self.serializer_class(self.get_object(pk)) 
        serialized_data = serializer.data
        print(serialized_data)

        return Response(serialized_data, status=status.HTTP_200_OK)


class Registration_for_customer(generics.GenericAPIView):

    serializer_class = RegistrationSerializer


    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "Message": "User created successfully",
                
                "User": serializer.data},status=status.HTTP_201_CREATED)
        return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#This is for login page 
class UserLogin(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    def post(self, request, *args, **kwargs):
        email = request.data['email']
        if email is None:
            return Response({'error': 'Email not informed'}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = User.objects.get(email=email)
            if not user.check_password(request.data['password']):
                return Response({'error': 'Email ou senha incorreto'}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({
                "Message": "login successfully",
                "user":RegistrationSerializer(user,
                context={'request': request}).data}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_403_FORBIDDEN)
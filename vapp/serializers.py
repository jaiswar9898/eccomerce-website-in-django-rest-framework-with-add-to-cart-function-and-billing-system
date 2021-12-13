from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
# from drf_writable_nested import WritableNestedModelSerializer
from .models import *


class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantityVariant
        fields = '__all__' 
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' 

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    quantity_type = QuantitySerializer()
    class Meta:
        model = Product
        fields = '__all__'
        
class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password')

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('username already exists')})

        return super().validate(args)

#     def create(self, validated_data):
#          return User.objects.create_user(**validated_data)

 # This set_password method will hide the password in admin panel 

    # def create(self, validated_data):
    #     user = User.objects.create(username = validated_data['username'])
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user
    
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],    # This create method will help to pass the all data in admin panel 
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])   # This will hide the password in admin panel in which other user can't see
        user.save()

        return user
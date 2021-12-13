from django.urls import path
from .views import *
from vapp.views import index,detail,ProductView,ProductView_singular


urlpatterns = [
    path('' , index),
    path('<int:id>',detail, name="detail"),
    path('products' , ProductView.as_view()),
    path('product/<int:pk>',ProductView_singular.as_view()),
    path('customer', Registration_for_customer.as_view(), name='customer'),
    path('login', UserLogin.as_view(), name='login'),
   
   
]

from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from vapp.models import Category,Product,QuantityVariant,ColorVariant,SizeVariant,ProductImages

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(QuantityVariant)
admin.site.register(ColorVariant)
admin.site.register(SizeVariant)
admin.site.register(ProductImages)

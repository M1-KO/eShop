from django.contrib import admin
from .models import Category, Order, Product, Cart, Review, ItemOrder

# Register your models here.
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Review)
admin.site.register(ItemOrder)
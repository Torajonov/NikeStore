from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'price']

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'total_sum','state', 'payed']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [ 'total_quantity', 'total_price']
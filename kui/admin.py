from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.db.models.aggregates import Count
from django.utils.html import format_html
from . import models

# Register your models here.

@admin.register(models.Customer)

class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','first_name', 'last_name', 'email','phone_number', 'orders']
    list_editable = ['first_name', 'last_name', 'email','phone_number']
    list_per_page = 10
    search_fields = ['first_name__istartswith', 'last_name__istartswith','phone_number']

    def orders(self, customer):
        return customer.orders

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(orders= Count('order'))


@admin.register(models.Product)

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','product_name','product_description','collection', 'product_price','product_inventory', 'inventory_status']
    list_editable = ['product_name', 'product_price','product_inventory']
    list_per_page = 10

    @admin.display(ordering = 'inventory_status')
    def inventory_status(self, product):
        if product.product_inventory == 0:
            return 'Out of Stock'
        return 'In Stock'

@admin.register(models.Collection)

class CollectionAdmin(admin.ModelAdmin):
    list_display=['id','title','featured_product']
    list_editable = ['title','featured_product']
    list_per_page = 10
    

@admin.register(models.Promotion)

class PromotionAdmin(admin.ModelAdmin):
    list_display=['id','description', 'discount']
    list_editable = ['description', 'discount']
    list_per_page = 10


 
@admin.register(models.Order)

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','customer', 'placed_at', 'payment_status','complete']
    list_editable = ['payment_status', 'complete']
    list_per_page = 10


@admin.register(models.Address)

class AddressAdmin(admin.ModelAdmin):
    list_display=['id', 'customer_id', 'area', 'town']
    list_editable = ['area', 'town']
    list_per_page = 10

@admin.register(models.CartItem)

class CartItemAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Cart)

class CartAdmin(admin.ModelAdmin):
    pass







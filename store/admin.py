from django.contrib import admin
from .models import Product, Order, ProductImage


# ORDER ADMIN
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'quantity', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'product__name')


# PRODUCT IMAGE INLINE
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


# PRODUCT ADMIN
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


# REGISTER ORDER ONLY
admin.site.register(Order, OrderAdmin)
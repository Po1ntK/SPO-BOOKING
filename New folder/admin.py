
from django.contrib import admin
from .models import Catagory, Product, Transaction

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Sku', 'Quantity', 'Unit_Price')

admin.site.register(Catagory)
admin.site.register(Transaction)


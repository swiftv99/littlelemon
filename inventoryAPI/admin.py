from django.contrib import admin

from inventoryAPI.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'company')
    list_filter = ('category', 'company')
    search_fields = ('name', 'description', 'company')
    ordering = ('name', 'price', 'company')
    
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
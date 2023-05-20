from django_filters.rest_framework import FilterSet

from inventoryAPI.models import Product

class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'company': ['exact'],
            'price': ['gte', 'lte'],
        }
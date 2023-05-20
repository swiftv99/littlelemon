from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from inventoryAPI.filters import ProductFilter
from inventoryAPI.models import Product, Category
from inventoryAPI.permissions import IsStaffOrReadOnly
from inventoryAPI.serializers import ProductSerializer, CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']
    
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price', 'created_at']
    # ordering = ['name']

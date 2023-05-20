from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from inventoryAPI.filters import ProductFilter
from inventoryAPI.models import Product, Category
from inventoryAPI.permissions import IsStaffOrReadOnly, IsStaff, IsCompany, IsClient
from inventoryAPI.serializers import CategorySerializer, ProductSerializer, AdminProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']
    
    
class ProductViewSet(viewsets.ModelViewSet):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsStaff | IsCompany | IsClient]
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price', 'created_at']
    # ordering = ['name']

    def get_queryset(self):
        queryset = Product.objects.select_related('company').all()
        role = getattr(self.request.user, "role", None)
        if role == "company":
            queryset = queryset.filter(company=self.request.user)
        return queryset
    
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return AdminProductSerializer
        return ProductSerializer
    
    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            serializer.save(company=self.request.user)
        serializer.save()
        
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# For caching
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from inventoryAPI.filters import ProductFilter
from inventoryAPI.models import Product, Category
from inventoryAPI.permissions import IsStaffOrReadOnly, IsStaff, IsCompany, IsClient
from inventoryAPI.serializers import CategorySerializer, ProductSerializer, AdminProductSerializer


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@method_decorator(cache_page(CACHE_TTL), name='dispatch')  
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']
    

@method_decorator(cache_page(CACHE_TTL), name='dispatch')  
class ProductViewSet(viewsets.ModelViewSet):
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
        
    def perform_update(self, serializer):
        if not self.request.user.is_staff:
            serializer.save(company=self.request.user)
        serializer.save()
        
    # @action(detail=True, methods=['get'])
    # def download_image(self, request, pk=None):
    #     product = self.get_object()
    #     if product.image:
    #         file_path = product.image.path
    #         with open(file_path, 'rb') as file:
    #             response = HttpResponse(file.read(), content_type='image/jpeg')
    #             response['Content-Disposition'] = 'attachment; filename=' + product.image.name
    #             return response
    #     else:
    #         return Response({'error': 'No image available for this product.'})
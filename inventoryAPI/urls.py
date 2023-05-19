from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, CategoryViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product'),
router.register(r'categories', CategoryViewSet, basename='category'),

urlpatterns = [
    path('', include(router.urls)),    
]

# urlpatterns = [
#     path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list'),
#     path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='product-detail'),
# ]

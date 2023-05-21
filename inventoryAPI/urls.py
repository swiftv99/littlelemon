from django.urls import path, include
from rest_framework.routers import SimpleRouter

from inventoryAPI.views import ProductViewSet, CategoryViewSet


router = SimpleRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [  
    path('', include(router.urls)),  
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from inventoryAPI.urls import router as inventory_router
from .views import RegisterAPIView, ChangePasswordAPIView, UserViewSet

router = DefaultRouter()

router.registry.extend(inventory_router.registry)
router.register(r'users', UserViewSet, basename="user")

urlpatterns = [    
    path('register/', RegisterAPIView.as_view(), name='user-registration'),
    path('change-password/', ChangePasswordAPIView.as_view(), name='change-password'),
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from fileuploadAPI.urls import router as fileupload_router
from inventoryAPI.urls import router as inventory_router
from thirdpartyAPI import views as thirdparytAPI_views
from userAPI.views import RegisterAPIView, ChangePasswordAPIView, UserViewSet


router = DefaultRouter()

router.registry.extend(fileupload_router.registry)
router.registry.extend(inventory_router.registry)
router.register(r'users', UserViewSet, basename="user")

urlpatterns = [    
    path('', include(router.urls)),
    path('auth/register/', RegisterAPIView.as_view(), name='user-registration'),
    path('auth/change-password/', ChangePasswordAPIView.as_view(), name='change-password'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/login/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('github/', thirdparytAPI_views.github, name='github'),  
    path('github/client/', thirdparytAPI_views.github_client, name='github_client'),
]
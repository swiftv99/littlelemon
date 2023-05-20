from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from userAPI.models import User
from userAPI.serializers import RegisterUserSerializer, ChangePasswordSerializer, CreateReadUserSerializer, UpdateUserSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    permission_classes = [IsAuthenticated]
    # filter_backends = [DjangoFilterBackend, OrderingFilter]
    # filterset_class = UserFilter
    # ordering_fields = ['id']

    def get_queryset(self):
        queryset = User.objects.all()
        is_staff = getattr(self.request.user, "is_staff", None)
        if not is_staff:
            queryset = queryset.filter(id=self.request.user.id)
        return queryset


    def get_serializer_class(self):
        if self.action in ["update", "partial_update"]:
            return UpdateUserSerializer
        return CreateReadUserSerializer
    
    
class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterUserSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordAPIView(generics.UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    
    def put(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

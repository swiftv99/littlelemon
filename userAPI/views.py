from rest_framework import status, viewsets
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from .serializers import UserSerializer, RegisterUserSerializer


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterUserSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserRegistrationAPIView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({'token': user.auth_token.key}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProductViewSet(viewsets.ModelViewSet):
#     # queryset = User.objects.all()
#     serializer_class = UserSerializer
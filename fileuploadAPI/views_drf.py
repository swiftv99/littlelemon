
from rest_framework import viewsets

from fileuploadAPI.models import Book
from fileuploadAPI.permissions import IsStaffOrReadOnly
from fileuploadAPI.serializers import BookSerializer

        
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsStaffOrReadOnly]
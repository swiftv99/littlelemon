from django.urls import path, include
from rest_framework.routers import SimpleRouter

from fileuploadAPI.views_drf import BookViewSet
# from fileuploadAPI import views


router = SimpleRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [  
    path('', include(router.urls)),  
]

# For Django Template View instead of Browsable API
# urlpatterns += [
#     path('books/', views.book_list, name='book_list'),
#     path('books/upload/', views.upload_book, name='upload_book'),
#     path('book/<int:pk>/', views.delete_book, name='delete_book'),
    
#     path('class/books/', views.BookListView.as_view(), name='class_book_list'),
#     path('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book')
# ]
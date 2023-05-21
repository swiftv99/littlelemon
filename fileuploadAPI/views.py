# from django.http import HttpResponse
# from rest_framework import viewsets
# For file uploading
# from rest_framework.decorators import api_view, action
# from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
# from django.core.files.storage import FileSystemStorage

from fileuploadAPI.forms import BookForm
from fileuploadAPI.models import Book


# @api_view()
# def hello_world(request):
#     return Response({"message": "Hello, world!"})

# def upload(request):
#     context = {}
#     if request.method == "POST":
#         uploaded_file = request.FILES['document']
#         fs = FileSystemStorage()
#         name = fs.save(uploaded_file.name, uploaded_file)
#         context['url'] = fs.url(name)
#     return render(request, 'upload.html', context)
    
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def upload_book(request):
    if request.method == "POST":    
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {'form': form})


def delete_book(request, pk):
    if request.method == "POST":
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')


class BookListView(ListView):
    model = Book
    template_name = 'class_book_list.html'
    context_object_name = 'books'
    
    
class UploadBookView(CreateView):
    model = Book
    fields = ['title', 'author', 'pdf', 'cover']
    success_url = reverse_lazy('class_book_list')
    template_name = 'upload_book.html'
    
    
# class UploadBookView(CreateView):
#     model = Book
#     form_class = BookForm
#     success_url = reverse_lazy('class_book_list')
#     template_name = 'upload_book.html'
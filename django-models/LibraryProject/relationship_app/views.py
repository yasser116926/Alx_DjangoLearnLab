from django.shortcuts import render, get_object_or_404
from .models import Book, Library
from django.views.generic import DetailView
from django.http import HttpResponse


# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

def home(request):
    return HttpResponse("Welcome , this is the homepage ")    
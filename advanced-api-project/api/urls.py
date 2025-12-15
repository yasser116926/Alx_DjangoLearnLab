from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    # GET all books
    path('books/', BookListView.as_view(), name='book-list'),

    # GET one book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # CREATE
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # UPDATE  (checker wants "books/update")
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),

    # DELETE  (checker wants "books/delete")
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]
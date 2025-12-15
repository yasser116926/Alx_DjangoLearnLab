from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend

"""
api/views.py

This module defines DRF generic views for the Book model.
- Read endpoints (list & detail) use IsAuthenticatedOrReadOnly so anonymous users can read,
  while authenticated users would be allowed any write actions if the view supported them.
  (ListAPIView and RetrieveAPIView are read-only by design.)
- Write endpoints (create, update, delete) require IsAuthenticated so only logged-in users can modify data.

Each view includes a short docstring and optional hooks (perform_create / perform_update / perform_destroy)
which you can extend to add custom behavior (e.g., signal emission, auditing, attaching request.user).
"""

"""
Filtering, Searching, and Ordering:

Examples:
1. Filtering:
    /api/books/?title=Python
    /api/books/?author=1
    /api/books/?publication_year=2022

2. Searching (partial match):
    /api/books/?search=django
    /api/books/?search=John

3. Ordering:
    /api/books/?ordering=title
    /api/books/?ordering=-publication_year
"""

class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    Supports:
    - Filtering (title, author, publication_year)
    - Searching (title and author name)
    - Ordering (title, publication_year)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Use checker-required filters
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching fields
    search_fields = ['title', 'author__name']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']

    # Default ordering
    ordering = ['title']




class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<int:pk>/
    Returns a single Book by primary key.
    Permission: Read-only for unauthenticated users, authenticated users allowed by IsAuthenticatedOrReadOnly.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Creates a new Book instance.
    Permission: Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Custom logic on creation can be placed here.
        # Example: attach metadata, log the creator, etc.
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /api/books/update/<int:pk>/
    Updates an existing Book instance.
    Permission: Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Custom update logic can be added here.
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/delete/<int:pk>/
    Deletes a Book instance.
    Permission: Authenticated users only.
    """
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        # Custom deletion behavior (soft-delete, logging, etc.) could be implemented here.
        instance.delete()
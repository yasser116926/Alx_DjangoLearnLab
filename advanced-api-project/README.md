# Book API Endpoints

This module provides CRUD operations for the Book model using Django REST Framework generic views.

Views implemented:

- BookListView: Returns all books (public).
- BookDetailView: Returns a single book by ID (public).
- BookCreateView: Creates a new book (authenticated users only).
- BookUpdateView: Updates an existing book (authenticated users only).
- BookDeleteView: Deletes a book (authenticated users only).

All views use DRF generic views and enforce model validation through BookSerializer.

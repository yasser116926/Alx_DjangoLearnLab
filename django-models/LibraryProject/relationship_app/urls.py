from django.urls import path
from .views import add_book, LibraryDetailView
from .views import edit_book, LibraryDetailView
from . import views

from .views import list_books
from .views import (
    list_books, LibraryDetailView, register,
    admin_view, librarian_view, member_view,
    add_book, edit_book, delete_book
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),
    path('register/', register, name='register'),

    # Role-based views
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),

    # Secured Book actions
    path('add_book/', add_book, name='add_book_alt'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book_alt'),

    path('books/delete/<int:pk>/', delete_book, name='delete_book'),
]
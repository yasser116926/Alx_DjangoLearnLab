from django.contrib import admin, list_books, LibraryDetailView
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('', include('relationship_app.urls')),
]
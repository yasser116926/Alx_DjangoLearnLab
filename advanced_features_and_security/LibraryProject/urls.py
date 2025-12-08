from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from .views import list_books, LibraryDetailView


def redirect_to_books(request):
    return redirect('list_books')

urlpatterns = [
    path('', redirect_to_books, name='root_redirect'),  
    path('admin/', admin.site.urls),
    path('books/', include('relationship_app.urls')),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

]

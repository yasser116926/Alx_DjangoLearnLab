from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_books(request):
    return redirect('list_books')

urlpatterns = [
    path('', redirect_to_books, name='root_redirect'),  
    path('admin/', admin.site.urls),
    path('books/', include('relationship_app.urls')),
]

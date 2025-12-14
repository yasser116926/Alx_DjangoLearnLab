from django.urls import path
from .views import book_list_api
from django.urls import path


urlpatterns = [
    path('books/', book_list_api, name='api_books'),
]

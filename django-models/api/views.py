
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from relationship_app.models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def book_list_api(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

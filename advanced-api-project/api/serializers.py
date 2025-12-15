from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# Serializer for the Book model.
# Includes custom validation to prevent future publication years.
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation method
    def validate_publication_year(self, value):
        current_year = datetime.now().year

        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


# Serializer for the Author model.
# Includes nested books, serialized using BookSerializer.
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer to show all books written by the author.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
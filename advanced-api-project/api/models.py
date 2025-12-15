from django.db import models

# Author model stores basic author information.
# One Author → Many Books (One-to-Many relationship)
class Author(models.Model):
    name = models.CharField(max_length=255)  # Name of the author

    def __str__(self):
        return self.name


# Book model stores book details.
# Each Book belongs to a single Author (ForeignKey)
class Book(models.Model):
    title = models.CharField(max_length=255)                       # Book title
    publication_year = models.IntegerField()                       # Year published
    author = models.ForeignKey(Author, on_delete=models.CASCADE,   # Relationship
                               related_name='books')

    def __str__(self):
        return self.title
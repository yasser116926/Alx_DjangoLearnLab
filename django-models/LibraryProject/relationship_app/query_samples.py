from .models import Author, Book, Library, Librarian


# 1. Get a library by name
def get_library_by_name(library_name):
    return Library.objects.get(name=library_name)


# 2. Get books written by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)


# 3. Retrieve the librarian for a given library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    # Assuming Library has OneToOneField or ForeignKey to Librarian
    return library.librarian

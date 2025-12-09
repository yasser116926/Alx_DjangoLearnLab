from .models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print("Books by author:", [book.title for book in books_by_author])

# 2. List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print("Books in library:", [book.title for book in books_in_library])

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian of library:", librarian.name)
from relationship_app.models import Author, Book, Library, Librarian

# -----------------------------------------
# 1. Get a Library by name
# -----------------------------------------
def get_library_by_name(library_name):
    return Library.objects.get(name=library_name)


# -----------------------------------------
# 2. Get all Books by a specific Author
# -----------------------------------------
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)      # required
    return Book.objects.filter(author=author)          # required


# -----------------------------------------
# 3. Retrieve the Librarian for a Library
# -----------------------------------------
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian  # assuming OneToOne: Library → Librarian


# -----------------------------------------
# 4. List all Books in a Library
# -----------------------------------------
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# -----------------------------------------
# 5. List all Libraries that contain a Book
# -----------------------------------------
def get_libraries_containing_book(book_title):
    book = Book.objects.get(title=book_title)
    return book.libraries.all()

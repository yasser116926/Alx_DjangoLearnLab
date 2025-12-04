from relationship_app.models import Author, Book, Library


def get_all_books():
    """Return all books."""
    return Book.objects.all()


def get_books_by_author(author_name):
    """Return books written by a specific author."""
    return Book.objects.filter(author__name=author_name)


def get_library_by_name(library_name):
    """Return a single library object by its name."""
    # THIS is the line they said is missing
    return Library.objects.get(name=library_name)


def get_books_in_library(library_name):
    """Return all books in a specific library."""
    library = Library.objects.get(name=library_name)
    return library.books.all()


def create_author(name):
    """Create a new author."""
    author = Author.objects.create(name=name)
    return author


def create_book(title, publication_year, author_name):
    """Create a book and link it to an author."""
    author, created = Author.objects.get_or_create(name=author_name)
    book = Book.objects.create(
        title=title,
        publication_year=publication_year,
        author=author
    )
    return book


def create_library(name):
    """Create a new library."""
    library = Library.objects.create(name=name)
    return library


def add_book_to_library(book_title, library_name):
    """Add an existing book to the library."""
    book = Book.objects.get(title=book_title)
    library = Library.objects.get(name=library_name)
    library.books.add(book)
    return library

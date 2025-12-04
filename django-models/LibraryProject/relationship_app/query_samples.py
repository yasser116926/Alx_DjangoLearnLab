from bookshelf.models import Author, Book, Library


def run_queries():

    print("\n--- All Books ---")
    for book in Book.objects.all():
        print(f"{book.title} by {book.author.name}")

    print("\n--- All Authors ---")
    for author in Author.objects.all():
        print(author.name)

    print("\n--- All Libraries ---")
    for library in Library.objects.all():
        print(library.name)

    print("\n--- Books in Each Library ---")
    for library in Library.objects.all():
        print(f"\nLibrary: {library.name}")
        for book in library.books.all():
            print(f"- {book.title} by {book.author.name}")

    print("\n--- Books published after 2010 ---")
    recent_books = Book.objects.filter(publication_year__gt=2010)
    for book in recent_books:
        print(f"{book.title} ({book.publication_year})")

    print("\n--- Books by a specific author (Example: Author ID=1) ---")
    try:
        author = Author.objects.get(id=1)
        books = Book.objects.filter(author=author)
        print(f"Books by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print("Author with ID=1 does not exist.")

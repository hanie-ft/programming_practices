from booklovers.books.models import Book


def create_book(
    *, title: str, author: str, publisher: str | None, category: str
) -> Book:
    print(f"in create_books: {title, author, publisher, category}")
    return Book.objects.create(
        title=title, author=author, publisher=publisher, category=category
    )

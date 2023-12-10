from django.db.models import QuerySet
from booklovers.books.models import Book


def get_books() -> QuerySet[Book]:
    return Book.objects.all()

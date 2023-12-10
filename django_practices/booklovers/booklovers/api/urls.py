from django.urls import path, include
from booklovers.books.apis.books import BookApi

urlpatterns = [
    path("book/", BookApi.as_view(), name="book"),
]

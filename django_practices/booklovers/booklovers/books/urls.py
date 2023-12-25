# from django.urls import path, include

# urlpatterns = [path("books/", include(("booklovers.books.urls", "books")))]
from django.urls import path, include
from booklovers.books.apis.books import BookApi

urlpatterns = [
    path('', BookApi.as_view(),name="book"),
]
from django.urls import path, include

urlpatterns = [path("books/", include(("booklovers.books.urls", "books")))]

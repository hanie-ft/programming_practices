from django.urls import path, include

urlpatterns = [
    path("books/", include(("booklovers.books.urls", "books"))),
    path("users/", include(("booklovers.users.urls", "users"))),
    path("auth/", include(("booklovers.authentication.urls", "auth"))),
]

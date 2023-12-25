# from django.urls import path, include
# from booklovers.books.apis.books import BookApi
# from booklovers.users.apis.users import RegisterUserApi

# urlpatterns = [
#     path("book/", BookApi.as_view(), name="book"),
#     path('users/', RegisterUserApi.as_view, name='users'),
#     # path('auth/', include(('booklovers.authentication.urls', 'auth'))),
# ]

from django.urls import path, include

urlpatterns = [
    path("books/", include(("booklovers.books.urls", "books"))),
    path("users/", include(("booklovers.users.urls", "users"))),
]

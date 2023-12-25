from django.urls import path
from .apis.users import ProfileApi, RegisterUserApi


urlpatterns = [
    path("register/", RegisterUserApi.as_view(), name="register"),
    path("profile/", ProfileApi.as_view(), name="profile"),
]

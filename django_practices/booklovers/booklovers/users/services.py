from django.db import transaction

from booklovers.users.models import CustomUser, Profile


def create_user(*, username: str, email: str, password: str) -> CustomUser:
    return CustomUser.objects.create_user(
        username=username, email=email, password=password
    )


def create_profile(*, user:CustomUser, bio:str | None) -> Profile:
    return Profile.objects.create(user=user, bio=bio)


@transaction.atomic
def registeruser(
    *, username: str, email: str, password: str, bio: str | None
) -> CustomUser:
    user = create_user(username=username, email=email, password=password)
    create_profile(user=user, bio=bio)

    return user

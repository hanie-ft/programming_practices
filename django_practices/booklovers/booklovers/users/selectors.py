from .models import CustomUser, Profile


def get_profile(user: CustomUser) -> Profile:
    return Profile.objects.get(user=user)

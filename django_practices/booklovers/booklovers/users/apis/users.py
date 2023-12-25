from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from booklovers.api.mixins import ApiAuthMixin
from booklovers.users.selectors import get_profile
from booklovers.users.models import CustomUser, Profile
from booklovers.users.services import registeruser
from booklovers.users.validators import (
    number_validator,
    special_char_validator,
    letter_validator,
)
from django.core.validators import MinLengthValidator
from drf_spectacular.utils import extend_schema


class ProfileApi(ApiAuthMixin, APIView):
    class OutPutProfileSerializer(serializers.ModelSerializer):
        username = serializers.CharField(read_only = True)

        class Meta:
            model = Profile
            fields = (
                "username",
                "created_at",
                "bio",
                "user_books_count",
                "connection_count",
            )

    @extend_schema(responses=OutPutProfileSerializer)
    def get(self, request):
        query = get_profile(user=request.user)
        return Response(self.OutPutProfileSerializer(query, context={"request": request}).data)


class RegisterUserApi(APIView):
    class InputRegisterSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=150)
        email = serializers.EmailField(max_length=255)
        bio = serializers.CharField(max_length=1000, required=False)
        password = serializers.CharField(
            validators=[
                number_validator,
                letter_validator,
                special_char_validator,
                MinLengthValidator(limit_value=10),
            ]
        )
        confirm_password = serializers.CharField(max_length=255)

    class OutPutRegisterSerializer(serializers.ModelSerializer):
        class Meta:
            model = CustomUser
            fields = ("username", "created_at", "updated_at")

    def validate_email(self, email):
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("email Already Taken")
        return email

    def validate(self, data):
        if not data.get("password") or not data.get("confirm_password"):
            raise serializers.ValidationError(
                "Please fill password and confirm password"
            )

        if data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError(
                "confirm password is not equal to password"
            )
        return data

    @extend_schema(request=InputRegisterSerializer, responses=OutPutRegisterSerializer)
    def post(self, request):
        input_serializer = self.InputRegisterSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        try:
            user = registeruser(
                email=input_serializer.validated_data.get("email"),
                username=input_serializer.validated_data.get("username"),
                password=input_serializer.validated_data.get("password"),
                bio=input_serializer.validated_data.get("bio"),
            )
        except Exception as ex:
            return Response(f"Database Error {ex}", status=status.HTTP_400_BAD_REQUEST)
        return Response(
            self.OutPutRegisterSerializer(user, context={"request": request}).data
        )

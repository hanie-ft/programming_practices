from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from booklovers.books.models import Book
from booklovers.books.services.books import create_book
from booklovers.books.selectors.books import get_books


class BookApi(APIView):
    class InputBookSerializers(serializers.Serializer):
        title = serializers.CharField(max_length=100)
        author = serializers.CharField(max_length=100)
        publisher = serializers.CharField(max_length=150)
        category = serializers.CharField(max_length=50)

    class OutPutBooksSerializers(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = (
                "title",
                "author",
                "publisher",
                "category",
                "created_at",
                "updated_at",
            )

    @extend_schema(request=InputBookSerializers, responses=OutPutBooksSerializers)
    def post(self, request):
        input_serializer = self.InputBookSerializers(data=request.data)
        print(f"input_serializer {input_serializer}")
        input_serializer.is_valid(raise_exception=True)
        print("after validation")
        try:
            query = create_book(
                title=input_serializer.validated_data.get("title"),
                author=input_serializer.validated_data.get("author"),
                publisher=input_serializer.validated_data.get("publisher"),
                category=input_serializer.validated_data.get("category"),
            )
        except Exception as ex:
            return Response(f"Database Error: {ex}", status=status.HTTP_400_BAD_REQUEST)

        return Response(
            self.OutPutBooksSerializers(query, context={"request": request}).data
        )

    @extend_schema(responses=OutPutBooksSerializers)
    def get(self, request):
        query = get_books()
        return Response(
            self.OutPutBooksSerializers(
                query, context={"request": request}, many=True
            ).data
        )

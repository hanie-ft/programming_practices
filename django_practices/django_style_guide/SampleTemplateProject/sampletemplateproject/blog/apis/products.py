from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from sampletemplateproject.blog.models import Product
from sampletemplateproject.blog.services.products import create_product
from sampletemplateproject.blog.selectors.products import get_all_products
from drf_spectacular.utils import extend_schema


class ProductApi(APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255)

    class OutPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ("name", "created_at", "updated_at")

    @extend_schema(request=InputSerializer, responses=OutPutSerializer)
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = create_product(name=serializer.validated_data.get("name"))
        except Exception as ex:
            return Response(
                    f"Database Error {ex}",
                    status=status.HTTP_400_BAD_REQUEST
                    )
        return Response(self.OutPutSerializer(query, context={"request":request}).data)

    @extend_schema(responses=OutPutSerializer)
    def get(self, request):
        query_products = get_all_products()
        return Response(
            self.OutPutSerializer(
                query_products, context={"request": request}, many=True
            ).data
        )

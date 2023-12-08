from django.db.models import QuerySet
from sampletemplateproject.blog.models import Product


def get_all_products() -> QuerySet[Product]:
    return Product.objects.all()

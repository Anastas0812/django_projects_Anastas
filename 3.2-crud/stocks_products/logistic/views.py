from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer





class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'description',]
    # при необходимости добавьте параметры фильтрации


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        product_id = self.request.query_params.get('products', None)

        if product_id is not None:
            # Фильтруем склады, которые имеют заданный продукт
            queryset = queryset.filter(positions__product_id=product_id).distinct()

        return queryset

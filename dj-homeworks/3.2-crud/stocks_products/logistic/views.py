from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'description',]


class StockViewSet(ModelViewSet):
    # queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    def get_queryset(self):
        queryset = Stock.objects.all()
        products = self.request.query_params.get('products')
        if products:
            queryset = queryset.filter(products__id=int(products))
        return queryset


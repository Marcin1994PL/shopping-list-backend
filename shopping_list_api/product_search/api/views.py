from rest_framework import viewsets, status
from rest_framework.response import Response

from product_search.ProductSearch import ProductSearch


class ProductSearchViewSet(viewsets.ViewSet):

    def search_by_barcode(self, request, barcode):
        product_search = ProductSearch()
        product = product_search.by_barcode(barcode)
        if product is not None:
            return Response(product)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def search_by_name(self, request, name):
        product_search = ProductSearch()
        product = product_search.by_name(name)
        if product is not None:
            return Response(product)
        return Response(status=status.HTTP_404_NOT_FOUND)
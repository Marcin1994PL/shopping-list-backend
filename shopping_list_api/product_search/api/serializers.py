from rest_framework import serializers

from product_search.ProductSearch import ProductSearch


# class ProductSearchSerializer(serializers.Serializer):
#     barcode = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return ProductSearch(validated_data['barcode'])
#
#     def update(self, instance, validated_data):
#         pass

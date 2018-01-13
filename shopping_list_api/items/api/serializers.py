from rest_framework import serializers

from items.models import Item
from lists.api.serializers import ShoppingListSerializer


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField(default=1)
    is_bought = serializers.BooleanField(default=False)
    list = ShoppingListSerializer(read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'name', 'quantity', 'is_bought', 'list')

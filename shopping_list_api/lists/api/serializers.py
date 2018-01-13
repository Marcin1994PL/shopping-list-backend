from rest_framework import serializers

from groups.api.serializers import ShoppingGroupUpdateDetailSerializer
from lists.models import ShoppingList


class ShoppingListCreateSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(max_length=100)
    group = ShoppingGroupUpdateDetailSerializer(read_only=True)

    class Meta:
        model = ShoppingList
        fields = ('name', 'group')

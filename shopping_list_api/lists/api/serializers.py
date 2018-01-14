from rest_framework import serializers

from groups.api.serializers import ShoppingGroupUpdateDetailSerializer
from lists.models import ShoppingList
from users.api.serializers import UserDetailSerializer


class ShoppingListSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    group = ShoppingGroupUpdateDetailSerializer(read_only=True)
    owner = UserDetailSerializer(read_only=True)

    class Meta:
        model = ShoppingList
        fields = ('id', 'name', 'group', 'owner')

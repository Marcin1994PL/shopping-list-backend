from rest_framework import generics

from groups.models import ShoppingGroup
from lists.api.serializers import ShoppingListCreateSerializer
from lists.models import ShoppingList


class ListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ShoppingListCreateSerializer

    def get_group(self):
        groupId = self.kwargs['groupId']
        return ShoppingGroup.objects.get(pk=groupId)

    def get_queryset(self):
        group = self.get_group()
        return ShoppingList.objects.filter(group=group)

    def perform_create(self, serializer):
        group = self.get_group()
        serializer.save(group=group)

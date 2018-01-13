from rest_framework import generics, status
from rest_framework.response import Response

from groups.models import ShoppingGroup
from lists.api.serializers import ShoppingListSerializer
from lists.models import ShoppingList


class ListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ShoppingListSerializer

    def get_group(self):
        group_id = self.kwargs['groupId']
        return ShoppingGroup.objects.get(pk=group_id)

    def get_queryset(self):
        group = self.get_group()
        return ShoppingList.objects.filter(group=group)

    def perform_create(self, serializer):
        group = self.get_group()
        owner = self.request.user
        serializer.save(group=group, owner=owner)


class ListDetailsUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ShoppingListSerializer

    def get_group(self):
        group_id = self.kwargs['groupId']
        return ShoppingGroup.objects.get(pk=group_id)

    def get_queryset(self):
        group = self.get_group()
        return ShoppingList.objects.filter(group=group)


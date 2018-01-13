from rest_framework import generics

from items.api.serializers import ItemSerializer
from items.models import Item
from lists.models import ShoppingList


class ItemListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_list(self):
        list_id = self.kwargs['listId']
        return ShoppingList.objects.get(pk=list_id)

    def get_queryset(self):
        query_list = self.get_list()
        return Item.objects.filter(list=query_list)

    def perform_create(self, serializer):
        query_list = self.get_list()
        serializer.save(list=query_list)


class ItemDetailsUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ItemSerializer

    def get_list(self):
        list_id = self.kwargs['listId']
        return ShoppingList.objects.get(pk=list_id)

    def get_queryset(self):
        query_list = self.get_list()
        return Item.objects.filter(list=query_list)


from django.core import exceptions
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from items.api.permissions import OnlyOwnerCanUpdate
from items.api.serializers import ItemSerializer
from items.models import Item
from lists.models import ShoppingList


class ItemListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get_list(self):
        list_id = self.kwargs['listId']
        return ShoppingList.objects.get(pk=list_id)

    def get_queryset(self):
        query_list = self.get_list()
        return Item.objects.filter(list=query_list)

    def perform_create(self, serializer):
        query_list = self.get_list()
        if self.request.user == query_list.owner:
            serializer.save(list=query_list)
        else:
            raise exceptions.PermissionDenied


class ItemDetailsUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ItemSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, OnlyOwnerCanUpdate,)

    def get_list(self):
        list_id = self.kwargs['listId']
        return ShoppingList.objects.get(pk=list_id)

    def get_queryset(self):
        query_list = self.get_list()
        return Item.objects.filter(list=query_list)


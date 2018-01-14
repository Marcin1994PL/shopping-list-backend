from django.core import exceptions
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from groups.models import ShoppingGroup
from lists.api.permissions import OnlyOwnerCanUpdate
from lists.api.serializers import ShoppingListSerializer
from lists.models import ShoppingList


class ListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ShoppingListSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get_group(self):
        group_id = self.kwargs['groupId']
        return ShoppingGroup.objects.get(pk=group_id)

    def get_queryset(self):
        group = self.get_group()
        return ShoppingList.objects.filter(group=group)

    def perform_create(self, serializer):
        group = self.get_group()
        owner = self.request.user
        if owner in group.members.all():
            serializer.save(group=group, owner=owner)
        else:
            raise exceptions.PermissionDenied

class ListDetailsUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ShoppingListSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, OnlyOwnerCanUpdate,)

    def get_group(self):
        group_id = self.kwargs['groupId']
        return ShoppingGroup.objects.get(pk=group_id)

    def get_queryset(self):
        group = self.get_group()
        return ShoppingList.objects.filter(group=group)


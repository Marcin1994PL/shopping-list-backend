from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from .serializers import (ShoppingGroupCreateSerializer, ShoppingGroupUpdateDetailSerializer,
                          ShoppingGroupMembersCreateListSerializer, ShoppingGroupMembersDetailDeleteSerializer)
from groups.models import ShoppingGroup
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import OnlyOwnerCanUpdate, OnlyGroupMemberCanSeeMembers
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class ShoppingGroupCreateListAPIView(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = ShoppingGroupCreateSerializer

    def get_queryset(self):
        queryset = ShoppingGroup.objects.all()

        if self.request.GET.get('name'):
            print(self.request.GET.get('name'))
            queryset = ShoppingGroup.objects.filter(name__icontains=self.request.GET.get('name'))
        return queryset


class ShoppingGroupDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ShoppingGroupUpdateDetailSerializer
    lookup_field = 'pk'
    queryset = ShoppingGroup.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, OnlyOwnerCanUpdate)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()  # here the object is retrieved
        serializer = self.get_serializer(instance)

        return Response(serializer.data)


class ShoppingGroupMembersCreateListAPIView(generics.ListCreateAPIView):
    serializer_class = ShoppingGroupMembersCreateListSerializer
    permission_classes = [OnlyGroupMemberCanSeeMembers, ]

    def get_serializer_context(self):
        group_id = self.kwargs['pk']
        return {'group_id': group_id,
                'request': self.request}

    def list(self, request, *args, **kwargs):
        queryset = ShoppingGroup.objects.get(pk=self.kwargs['pk'])

        serializer = self.get_serializer(queryset, many=False)
        return Response(serializer.data)


class ShoppingGroupMembersDetailDeleteApiView(generics.RetrieveDestroyAPIView):
    serializer_class = ShoppingGroupMembersDetailDeleteSerializer
    permission_classes = (OnlyOwnerCanUpdate, IsAuthenticated)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()  # here the object is retrieved
        if instance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        print('retrieve')
        return Response(serializer.data)

    def get_object(self):
        user_id = self.kwargs['user_id']

        shopping_group = ShoppingGroup.objects.get(pk=self.kwargs['pk'])
        members = shopping_group.members.all()
        member = get_object_or_404(members, pk=user_id)
        return member

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  # here the object is retrieved
        shopping_group = ShoppingGroup.objects.get(pk=self.kwargs['pk'])
        shopping_group.members.remove(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

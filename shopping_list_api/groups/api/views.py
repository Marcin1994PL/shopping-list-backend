from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from .serializers import ShoppingGroupCreateSerializer, ShoppingGroupUpdateDetailSerializer
from groups.models import ShoppingGroup
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import OnlyOwnerCanUpdate


class GroupCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = ShoppingGroupCreateSerializer

    def get_queryset(self):
        queryset = ShoppingGroup.objects.all()

        if self.request.GET.get('name'):
            print(self.request.GET.get('name'))
            queryset = ShoppingGroup.objects.filter(name__icontains=self.request.GET.get('name'))
        return queryset


class GroupDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ShoppingGroupUpdateDetailSerializer
    lookup_field = 'pk'
    queryset = ShoppingGroup.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, OnlyOwnerCanUpdate)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()  # here the object is retrieved
        serializer = self.get_serializer(instance)

        return Response(serializer.data)

from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ShoppingGroupCreateSerializer
from groups.models import ShoppingGroup


class GroupCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = ShoppingGroupCreateSerializer
    queryset = ShoppingGroup.objects.all()

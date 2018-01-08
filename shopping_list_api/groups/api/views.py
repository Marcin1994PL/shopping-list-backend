from rest_framework import views, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ShoppingGroupCreateSerializer


class GroupCreateAPIView(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = ShoppingGroupCreateSerializer


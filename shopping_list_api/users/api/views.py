from .serializers import UserCreateSerializer, UserLoginSerializer, UserDetailSerializer, UserUpdateSerializer
from rest_framework.response import Response
from rest_framework import generics, views, status
from django.contrib.auth.models import User


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = []


class UserLoginAPIView(views.APIView):
    """
    Endpoint for user login. Returns authentication token on success.
    """

    serializer_class = UserLoginSerializer
    permission_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPIView(generics.RetrieveAPIView):

    serializer_class = UserDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()  # here the object is retrieved
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_object(self):
        return self.request.user


class UserUpdateAPIView(generics.UpdateAPIView):

    serializer_class = UserUpdateSerializer

    def get_object(self):
        return self.request.user

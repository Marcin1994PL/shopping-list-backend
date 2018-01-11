from .serializers import UserCreateSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework import generics, views, status


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

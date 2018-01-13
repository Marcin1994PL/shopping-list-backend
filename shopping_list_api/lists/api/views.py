from rest_framework import generics

from lists.api.serializers import ShoppingListCreateSerializer
from lists.models import ShoppingList


class ListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ShoppingListCreateSerializer

    def get_queryset(self):
        queryset = ShoppingList.objects.all()

        # if self.request.GET.get('name'):
        #     print(self.request.GET.get('name'))
        #     queryset = ShoppingList.objects.filter(name__icontains=self.request.GET.get('name'))
        return queryset
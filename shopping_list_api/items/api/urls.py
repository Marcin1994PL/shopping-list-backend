from django.conf.urls import url

from items.api.views import ItemListCreateAPIView, ItemDetailsUpdateDeleteAPIView

urlpatterns = [
    url(r'^$', ItemListCreateAPIView.as_view(), name='create'),
    url(r'(?P<pk>\d+)$', ItemDetailsUpdateDeleteAPIView.as_view(), name='detail-update-delete'),
]

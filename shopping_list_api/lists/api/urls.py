from django.conf.urls import url

from lists.api.views import ListCreateAPIView, ListDetailsUpdateDeleteAPIView

urlpatterns = [
    url(r'^$', ListCreateAPIView.as_view(), name='create'),
    url(r'(?P<pk>\d+)$', ListDetailsUpdateDeleteAPIView.as_view(), name='detail-update-delete')
]

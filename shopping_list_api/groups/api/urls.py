from django.conf.urls import url
from .views import GroupCreateAPIView, GroupDetailUpdateAPIView
urlpatterns = [
    url(r'^$', GroupCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', GroupDetailUpdateAPIView.as_view(), name="detail-update"),
]

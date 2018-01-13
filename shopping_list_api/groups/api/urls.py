from django.conf.urls import url, include
from .views import GroupCreateAPIView, GroupDetailUpdateAPIView

urlpatterns = [
    url(r'^$', GroupCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', GroupDetailUpdateAPIView.as_view(), name="detail-update"),
    url(r'^api/groups/(?P<groupId>\d+)/lists/$', include('lists.api.urls', namespace='api-groups'))
]

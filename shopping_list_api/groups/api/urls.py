from django.conf.urls import url
from .views import GroupCreateAPIView
urlpatterns = [
    url(r'^$', GroupCreateAPIView.as_view(), name='create'),
]

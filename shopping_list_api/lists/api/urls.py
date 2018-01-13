from django.conf.urls import url

from lists.api.views import ListCreateAPIView

urlpatterns = [
    url(r'^$', ListCreateAPIView.as_view(), name='create')
]

from django.conf.urls import url
from .views import (ShoppingGroupCreateListAPIView, ShoppingGroupDetailUpdateAPIView,
                    ShoppingGroupMembersCreateListAPIView, ShoppingGroupMembersDetailDeleteApiView)
urlpatterns = [
    url(r'^$', ShoppingGroupCreateListAPIView.as_view()),
    url(r'^(?P<pk>\d+)/$', ShoppingGroupDetailUpdateAPIView.as_view()),
    url(r'^(?P<pk>\d+)/members/(?P<user_id>\d+)/$', ShoppingGroupMembersDetailDeleteApiView.as_view()),
    url(r'^(?P<pk>\d+)/members/$', ShoppingGroupMembersCreateListAPIView.as_view()),
]

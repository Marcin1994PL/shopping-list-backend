from django.conf.urls import url
from .views import UserCreateAPIView, UserLoginAPIView, UserDetailAPIView, UserUpdateAPIView
urlpatterns = [
    url(r'^add', UserCreateAPIView.as_view(), name='create'),
    url(r'^login', UserLoginAPIView.as_view(), name='login'),
    url(r'^detail', UserDetailAPIView.as_view(), name='login'),
    url(r'^edit', UserUpdateAPIView.as_view(), name='login')
]

from django.conf.urls import url

from product_search.api.views import ProductSearchViewSet

urlpatterns = [
    url(r'^barcode/(?P<barcode>\d+)$', ProductSearchViewSet.as_view({'get': 'search_by_barcode'}), name='barcode-search'),
    url(r'^name/(?P<name>[\w\-]+)$', ProductSearchViewSet.as_view({'get': 'search_by_name'}), name='name-search'),
]

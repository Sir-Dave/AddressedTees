from django.urls import re_path, path
from product.views import ProductRetrieveView, ProductListView

app_name = "product"
urlpatterns = [
    re_path("(?P<id>\d+)/", ProductRetrieveView.as_view(), name="products-rud"),
    re_path("", ProductListView.as_view(), name="product-create"),
]


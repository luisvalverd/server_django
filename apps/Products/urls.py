
from django.urls import path
from .views import (
    ProdutctListView, 
    ProductDelete,
    ProductUpdate,
    create_product,
)

urlpatterns = [
    path("products/", ProdutctListView.as_view(), name="products_list"),
    path("add-product/", create_product, name="add_product"),
    path('product/<int:id>/delete/', ProductDelete.as_view(), name="delete_product"),
    path('product/<int:id>/update/', ProductUpdate.as_view(), name="update_product"),
]
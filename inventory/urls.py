# inventory/urls.py

from django.urls import path
from .views import (
    inventory_list,
    per_product_view,
    add_product,
    delete_product,
    update_product,
    export_csv,
    search_products,
    search_results,
)

urlpatterns = [
    path("", inventory_list, name="inventory_list"),
    path("product/<int:pk>", per_product_view, name="per_product"),
    path("add_inventory/", add_product, name="add_inventory"),
    path("delete/<int:pk>", delete_product, name="delete_inventory"),
    path("update/<int:pk>", update_product, name="update_inventory"),
    path("export_csv/", export_csv, name="export_csv"),
    path("search/", search_products, name="search_products"),
    path("search_results/", search_results, name="search_results"),
]

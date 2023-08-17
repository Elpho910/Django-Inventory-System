# inventory/urls.py

from django.urls import path
from .views import inventory_list, per_product_view, add_product, delete_product, update_product, export_csv

urlpatterns = [
    path("", inventory_list, name="inventory_list"),
    path("product/<int:pk>", per_product_view, name="per_product"),
    path("add_inventory/", add_product, name="add_inventory"),
    path("delete/<int:pk>", delete_product, name="delete_inventory"),
    path("update/<int:pk>", update_product, name="update_inventory"),
    path('export_csv/', export_csv, name='export_csv'),
]

# inventory/forms.py

from django.forms import ModelForm
from .models import Inventory


class AddInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = [
            "brand",
            "title",
            "manufacturer_part_number",
            "barcode",
            "category",
            "cost_price",
            "quantity_in_stock",
            "description",
        ]


class UpdateInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = [
            "brand",
            "title",
            "manufacturer_part_number",
            "barcode",
            "category",
            "cost_price",
            "quantity_in_stock",
            "description",
        ]

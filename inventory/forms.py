# inventory/forms.py

from django.forms import ModelForm
from .models import Inventory
from django import forms


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


class PickingForm(forms.Form):
    code = forms.CharField(label="Barcode/Part Number", max_length=300)
    quantity = forms.IntegerField(label="Quantity", min_value=1)

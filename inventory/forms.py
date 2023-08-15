# inventory/forms.py

from django.forms import ModelForm
from .models import Inventory


class AddInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['manufacturer', 'name', 'item_code', 'cost_price', 'quantity_in_stock', 'description']


class UpdateInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['manufacturer', 'name', 'item_code', 'cost_price', 'quantity_in_stock', 'description']

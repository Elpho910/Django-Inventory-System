from django.shortcuts import get_object_or_404, render
from .models import Inventory
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def inventory_list(request):
    inventories = Inventory.objects.all()
    context = {
        "title": "Inventory List",
        "inventories": inventories
    }
    return render(request, "inventory_list.html", context=context)


@login_required()
def per_product_view(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    context = {
        'inventory': inventory
    }
    return render(request, "per_product.html", context=context)

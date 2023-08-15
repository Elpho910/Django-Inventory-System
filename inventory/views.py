from django.shortcuts import get_object_or_404, render, redirect
from .models import Inventory
from django.contrib.auth.decorators import login_required
from .forms import AddInventoryForm, UpdateInventoryForm

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


@login_required()
def add_product(request):
    if request.method == "POST":
        add_form = AddInventoryForm(data=request.POST)
        if add_form.is_valid():
            add_form.save(commit=True)
            return redirect("/inventory/")
    else:
        add_form = AddInventoryForm()

    return render(request, "inventory_add.html", {"form": add_form})


@login_required()
def delete_product(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    inventory.delete()
    return redirect("/inventory/")


@login_required()
def update_product(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        update_form = UpdateInventoryForm(data=request.POST)
        if update_form.is_valid():
            inventory.manufacturer = update_form.data['manufacturer']
            inventory.name = update_form.data['name']
            inventory.item_code = update_form.data['item_code']
            inventory.cost_price = update_form.data['cost_price']
            inventory.quantity_in_stock = update_form.data['quantity_in_stock']
            inventory.save()
            return redirect(f"/inventory/product/{pk}")
    else:
        update_form = UpdateInventoryForm(instance=inventory)

    context = {"form": update_form}
    return render(request, "inventory_update.html", context=context)



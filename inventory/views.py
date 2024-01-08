from django.shortcuts import get_object_or_404, render, redirect
from .models import Inventory
from django.contrib.auth.decorators import login_required
from .forms import AddInventoryForm, UpdateInventoryForm, PickingForm
import csv
from django.http import HttpResponse
from django.db.models import Q
from django.core import management


# Create your views here.


@login_required()
def inventory_list(request):
    inventories = Inventory.objects.all()
    context = {"title": "Inventory List", "inventories": inventories}
    return render(request, "inventory_list.html", context=context)


@login_required()
def per_product_view(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    context = {"inventory": inventory}
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
            inventory.brand = update_form.data["brand"]
            inventory.title = update_form.data["title"]
            inventory.manufacturer_part_number = update_form.data[
                "manufacturer_part_number"
            ]
            inventory.barcode = update_form.data["barcode"]
            inventory.category = update_form.data["category"]
            inventory.cost_price = update_form.data["cost_price"]
            inventory.quantity_in_stock = update_form.data["quantity_in_stock"]
            inventory.save()
            return redirect(f"/inventory/product/{pk}")
    else:
        update_form = UpdateInventoryForm(instance=inventory)

    context = {"form": update_form}
    return render(request, "inventory_update.html", context=context)


@login_required()
def search_products(request):
    return render(request, "inventory_search.html")


@login_required()
def search_results(request):
    query = request.GET.get("query", "")
    if query:
        results = Inventory.objects.filter(
            Q(brand__icontains=query)
            | Q(title__icontains=query)
            | Q(manufacturer_part_number__icontains=query)
            | Q(barcode__icontains=query)
            | Q(category__icontains=query)
            | Q(cost_price__icontains=query)
            | Q(quantity_in_stock__icontains=query)
            | Q(description__icontains=query)
        )
    else:
        results = []

    return render(request, "search_results.html", {"results": results})


def export_csv_kqm(request):
    management.call_command("export_inventory")

    return render(request, "export_result.html")


@login_required()
def export_csv(request):
    # Define the response object with appropriate headers for a CSV file
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="current_stock.csv"'

    # Create a CSV writer object
    writer = csv.writer(response)

    # Write the header row
    writer.writerow(
        [
            "Brand",
            "Title",
            "Manufacturer Part Number",
            "Barcode",
            "Category",
            "Cost",
            "Stock",
            "Description",
        ]
    )

    # Query all items from the database
    items = Inventory.objects.all()

    # Write the item data to the CSV file
    for item in items:
        writer.writerow(
            [
                item.brand,
                item.title,
                item.manufacturer_part_number,
                item.barcode,
                item.category,
                item.cost_price,
                item.quantity_in_stock,
                item.description,
            ]
        )

    return response


def picking_view(request):
    if request.method == "POST":
        form = PickingForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            quantity = form.cleaned_data["quantity"]

            # Search DB for barcode or part number entered
            item = Inventory.objects.filter(
                Q(barcode=code) | Q(manufacturer_part_number=code)
            ).first()

            if item and item.quantity_in_stock >= quantity:
                item.quantity_in_stock -= quantity
                item.save()

    else:
        form = PickingForm()

    return render(request, "picking_form.html", {"form": form})

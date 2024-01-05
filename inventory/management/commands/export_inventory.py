# inventory/management/commands/export_inventory.py


from django.core.management.base import BaseCommand
from inventory.models import Inventory
import csv


class Command(BaseCommand):
    help = "Exports inventory to a CSV file"

    def handle(self, *args, **kwargs):
        with open("inventory.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "Brand",
                    "Title",
                    "Manufacturer Part Number",
                    "Barcode",
                    "Quantity In Stock",
                    "Description",
                ]
            )
            items = Inventory.objects.all()
            for item in items:
                writer.writerow(
                    [
                        item.brand,
                        item.title,
                        item.manufacturer_part_number,
                        item.barcode,
                        item.cost_price,
                        item.quantity_in_stock,
                        item.description,
                    ]
                )

        self.stdout.write(self.style.SUCCESS("Successfully exported inventory to CSV"))

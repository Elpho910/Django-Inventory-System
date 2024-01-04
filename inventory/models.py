from django.db import models

# Create your models here.


class Inventory(models.Model):
    brand = models.CharField(max_length=300, null=False, blank=False)
    title = models.CharField(max_length=300, null=False, blank=False)
    manufacturer_part_number = models.CharField(max_length=300, null=False, blank=False)
    barcode = models.CharField(max_length=300, null=False, blank=False)
    cost_price = models.DecimalField(
        max_digits=19, decimal_places=2, null=False, blank=False
    )
    quantity_in_stock = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

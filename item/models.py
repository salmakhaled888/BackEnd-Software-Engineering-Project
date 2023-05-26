from django.db import models

# Create your models here.
class Item(models.Model):
    itemName = models.CharField(max_length=100)  # column
    description = models.TextField(max_length=1000)
    barcode_id = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=19, decimal_places=4)
    photo = models.ImageField(upload_to='Item')  # max_length=50
    # reorder =
    inStock = models.IntegerField(default=0)

    # category = models.ForeignKey()

    def str(self):
        return self.itemName
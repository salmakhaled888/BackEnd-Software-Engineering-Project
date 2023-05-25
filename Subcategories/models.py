from django.db import models

class subCategories(models.Model):
    name = models.CharField()
    category = models.models.ForeignKey(Categories, on_delete=models.CASCADE)
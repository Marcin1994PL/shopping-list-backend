from django.db import models
from lists.models import ShoppingList
# Create your models here.


class Item(models.Model):
    list = models.ForeignKey(ShoppingList)
    name = models.CharField(max_length=100, null=False, blank=False)
    quantity = models.IntegerField()
    is_bought = models.BooleanField()

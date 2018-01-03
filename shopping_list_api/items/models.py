from django.db import models
from lists.models import ShoppingList
# Create your models here.


class Item(models.Model):
    list = models.ForeignKey(ShoppingList)
    name = models.CharField(max_length=100, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

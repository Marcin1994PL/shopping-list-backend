from django.db import models
from lists.models import ShoppingList
# Create your models here.


class Item(models.Model):
    list = models.ForeignKey(ShoppingList)

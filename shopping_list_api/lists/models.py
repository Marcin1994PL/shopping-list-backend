from django.db import models
from groups.models import ShoppingGroup
# Create your models here.


class ShoppingList(models.Model):
    group = models.ForeignKey(ShoppingGroup)

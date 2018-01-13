from django.db import models
from groups.models import ShoppingGroup
# Create your models here.


class ShoppingList(models.Model):
    group = models.ForeignKey(ShoppingGroup)
    name = models.CharField(max_length=100, null=False, blank=False)


from django.db import models
from groups.models import ShoppingGroup
# Create your models here.


class ShoppingList(models.Model):
    group = models.ForeignKey(ShoppingGroup)
    name = models.CharField(max_length=100, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

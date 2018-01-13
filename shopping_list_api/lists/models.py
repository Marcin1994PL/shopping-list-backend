from django.contrib.auth.models import User
from django.db import models
from groups.models import ShoppingGroup
# Create your models here.


class ShoppingList(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    group = models.ForeignKey(ShoppingGroup)
    owner = models.ForeignKey(User)


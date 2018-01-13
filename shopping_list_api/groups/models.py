from django.db import models
from django.contrib.auth.models import User


class ShoppingGroup(models.Model):
    owner = models.ForeignKey(User, related_name="owner")
    members = models.ManyToManyField(User, related_name="member")
    name = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=10, null=False, blank=False)

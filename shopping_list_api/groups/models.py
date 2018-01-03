from django.db import models
from users.models import User
# Create your models here.


class ShoppingGroup(models.Model):
    owner = models.ForeignKey(User, related_name="owner")
    members = models.ManyToManyField(User, related_name="member")
    name = models.CharField(max_length=100, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

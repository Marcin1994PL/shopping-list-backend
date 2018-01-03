from django.db import models
from users.models import User
# Create your models here.


class ShoppingGroup(models.Model):
    owner = models.ForeignKey(User, related_name="owner")
    members = models.ManyToManyField(User, related_name="member")

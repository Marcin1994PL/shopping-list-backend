from rest_framework import permissions

from groups.models import ShoppingGroup
from lists.models import ShoppingList

OWNER_METHODS = ['POST', 'PUT', 'PATCH']


class OnlyOwnerCanUpdate(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.method not in OWNER_METHODS) or (obj.owner == request.user)


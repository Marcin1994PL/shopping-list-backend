from rest_framework import permissions
from groups.models import ShoppingGroup

OWNER_METHODS = ['POST', 'PUT', 'PATCH']

class OnlyGroupMemberCanSeeMembers(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method == "POST":
            return True
        shopping_group = ShoppingGroup.objects.filter(pk=request.resolver_match.kwargs.get('pk'), members__pk=request.user.pk)
        if shopping_group.exists():
            return True
        else:
            return False


class OnlyOwnerCanUpdate(permissions.BasePermission):

    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        shopping_group = ShoppingGroup.objects.get(pk=pk)
        if shopping_group.owner.pk == request.user.pk:
            is_owner = True

        if request.method in OWNER_METHODS:
            return is_owner
        else:
            return True




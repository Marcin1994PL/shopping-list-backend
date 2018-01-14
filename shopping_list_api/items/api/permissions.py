from rest_framework import permissions

OWNER_METHODS = ['POST', 'PUT', 'PATCH']


class OnlyOwnerCanUpdate(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.method not in OWNER_METHODS) or (obj.list.owner == request.user)


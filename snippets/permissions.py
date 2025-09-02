from rest_framework import permissions


class isOwnerOrReadOnly(permissions.BasePermission):
    """
    custom perm to allow only owner of obj to edit it
    """

    def has_object_permission(self, request, view, obj):
        # read permissions allowed for any reqs
        if request.method in permissions.SAFE_METHODS:
            return True
        ##unsafe reqs (putpostdel) only owner
        return obj.owner == request.user
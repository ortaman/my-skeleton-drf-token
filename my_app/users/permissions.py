
from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermissions(BasePermission):

    def has_permission(self, request, view):
        """
         - POST: Alloy any
         - All HTTP methods: If is authenticated
        """
        if request.method == 'POST' or request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
         - retrieve (admin): only admins
         - retrieve (user): admins and user.
         - update: itself user
        """
        if view.action == 'retrieve':
            if not request.user.is_staff and obj.is_staff:
                return False

        if request.method in SAFE_METHODS:  # GET, HEAD or OPTIONS
            return True

        return request.user == obj


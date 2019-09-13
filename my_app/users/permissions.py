
from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermissions(BasePermission):

    def has_permission(self, request, view):
        """
         - POST: Alloy any
         - All HTTP methods: If is authenticated and is not admin
        """

        # All can create a users
        if request.method == 'POST':
            return True

        # Admin dont have permission to the endponints
        elif request.user.is_staff:
            return False

        elif request.user.is_authenticated:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        """
         - retrieve: admins and user.
         - update: itself user
        """
        if request.method in SAFE_METHODS:  # GET, HEAD or OPTIONS
            return True

        return request.user == obj

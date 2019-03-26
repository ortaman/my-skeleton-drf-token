
from .models import User


class ApiUserBackend:

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # authenticate from django admin
            # if not (hasattr(request, 'path') and not request.path == '/admin/login/':
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            pass

        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def user_can_authenticate(self, user):
        """
        Reject users with is_active=False. Custom user models that don't have
        that attribute are allowed.
        """
        is_active = getattr(user, 'is_active', None)
        return is_active or is_active is None

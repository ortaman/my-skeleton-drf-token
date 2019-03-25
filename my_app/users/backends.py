

from django.contrib.auth.backends import ModelBackend
from .models import AdminUser, User


class CustomModelBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # authenticate from django admin
            if hasattr(request, 'path') and request.path == '/admin/login/':
                UserModel = AdminUser

            # authenticate from api
            elif True:
                UserModel = User

            user = UserModel.objects.get(username=username)

        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            if hasattr(request, 'path') and request.path == '/admin/login/':
                UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

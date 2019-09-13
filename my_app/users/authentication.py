
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import exceptions
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model

from common.utils import get_object_or_none

from .models import User


jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class JWTAuthentication(JSONWebTokenAuthentication):
    def authenticate_credentials(self, payload):
        """
        Returns an active user that matches the payload's user id and email.
        """
        username = jwt_get_username_from_payload(payload)

        if not username:
            msg = _('Invalid payload.')
            raise exceptions.AuthenticationFailed(msg)

        user = get_object_or_none(User, username=username)
        admin = get_object_or_none(get_user_model(), username=username)

        if not user and not admin:
            msg = _('Invalid user.')
            raise exceptions.AuthenticationFailed(msg)

        model = user if user else admin

        if not model.is_active:
            msg = _('User account is disabled.')
            raise exceptions.AuthenticationFailed(msg)

        return model

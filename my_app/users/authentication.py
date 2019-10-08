
from calendar import timegm
from datetime import datetime

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import exceptions
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from common.utils import get_object_or_none
from .models import User


def jwt_payload_handler_custom(user):

    payload = {
        'id': user.id,
        'name': user.get_full_name(),
    }

    # Include original issued at time for a brand new token,
    # to allow token refresh
    if api_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(
            datetime.utcnow().utctimetuple()
        )

    if api_settings.JWT_AUDIENCE is not None:
        payload['aud'] = api_settings.JWT_AUDIENCE

    if api_settings.JWT_ISSUER is not None:
        payload['iss'] = api_settings.JWT_ISSUER

    return payload


def create_jwt(model):

    jwt_payload_handler = jwt_payload_handler_custom
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(model)
    token = jwt_encode_handler(payload)

    return token


class JWTAuthentication(JSONWebTokenAuthentication):
    def authenticate_credentials(self, payload):
        """
        Returns an active user that matches the payload's user id and email.
        """
        id = payload.get('id')

        if not id:
            msg = _('Invalid payload.')
            raise exceptions.AuthenticationFailed(msg)

        user = get_object_or_none(User, id=id)
        admin = get_object_or_none(get_user_model(), id=id)

        if not user and not admin:
            msg = _('Invalid user.')
            raise exceptions.AuthenticationFailed(msg)

        model = user if user else admin

        if not model.is_active:
            msg = _('User account is disabled.')
            raise exceptions.AuthenticationFailed(msg)

        return model

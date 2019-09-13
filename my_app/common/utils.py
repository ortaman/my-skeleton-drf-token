
from calendar import timegm
from datetime import datetime

from rest_framework_jwt.settings import api_settings


def get_object_or_none(model, *args, **kwargs):
    try:
        obj = model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        obj = None
    return obj


def custom_jwt_payload_handler(user):

    payload = {
        'id': user.id,
        'username': user.username,
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

    jwt_payload_handler = custom_jwt_payload_handler

    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(model)
    token = jwt_encode_handler(payload)

    return token

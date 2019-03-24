from rest_framework_jwt.settings import api_settings


def get_object_or_none(model, *args, **kwargs):
    try:
        obj = model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        obj = None
    return obj


def create_jwt(model):

    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(model)
    token = jwt_encode_handler(payload)

    return token

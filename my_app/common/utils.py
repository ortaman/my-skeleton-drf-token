
def get_object_or_none(model, *args, **kwargs):
    try:
        obj = model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        obj = None
    return obj


from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name=_('Date of creation'))
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name=_('Date of the last update'))

    class Meta:
        abstract = True


from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import AbstractBaseModel


class Category(AbstractBaseModel):
    name = models.CharField(max_length=16, verbose_name=_('name'))

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name


class Skill(AbstractBaseModel):
    name = models.CharField(max_length=16, verbose_name=_('name'))
    skill = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("name")
        verbose_name_plural = _("names")

    def __str__(self):
        return self.name

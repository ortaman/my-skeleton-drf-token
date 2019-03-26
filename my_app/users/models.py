
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import check_password, make_password

from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _

from common.models import AbstractBaseModel


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    Username and password are required. Other fields are optional.
    """
    GENDER = (
        ('masculino', 'masculino'),
        ('femenino', 'femenino'),
    )
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=128,
        unique=True,
        help_text=_('Required. 128 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(max_length=128, verbose_name=_('email'))
    names = models.CharField(max_length=64, verbose_name=_('names'))
    surnames = models.CharField(max_length=64, verbose_name=_('surnames'))

    phone = models.CharField(max_length=22, verbose_name=_('phone'))
    gender = models.CharField(max_length=9, verbose_name=_('gender'), choices=GENDER)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('base_user')
        verbose_name_plural = _('base_users')
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.names, self.surnames)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.surnames

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Administrator(AbstractUser, AbstractBaseModel):

    class Meta:
        verbose_name = _("Administrator")
        verbose_name_plural = _("Administrators")

    def __str__(self):
        return "%s" % (self.get_full_name())


class User(AbstractBaseModel):
    GENDER = (
        ('masculino', 'masculino'),
        ('femenino', 'femenino'),
    )

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=128,
        unique=True,
        verbose_name=_('username'),
        help_text=_('Required. 128 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={'unique': _("A user with that username already exists.")},
    )
    password = models.CharField(_('password'), max_length=128)
    email = models.EmailField(max_length=128, verbose_name=_('email'))
    names = models.CharField(max_length=64, verbose_name=_('names'))
    surnames = models.CharField(max_length=64, verbose_name=_('surnames'))

    phone = models.CharField(max_length=22, verbose_name=_('phone'))
    gender = models.CharField(max_length=9, verbose_name=_('gender'), choices=GENDER)

    is_active = models.BooleanField(default=True, verbose_name=_('active'),)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)

    @property
    def is_authenticated(self):
        return True

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        full_name = '%s %s' % (self.names, self.surnames)
        return full_name.strip()

from django.db import models
from django.contrib import auth
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.utils.html import mark_safe

from django.utils.functional import lazy

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()


class Customer(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=30, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        ordering = ["-id"]
        verbose_name = "İstifadəçi"
        verbose_name_plural = "İstifadəçilər"

    objects = UserManager()


class Message(models.Model):
    name = models.CharField("Ad",max_length=50)
    email = models.EmailField("Email", max_length=250)
    phone_number = models.CharField("Əlaqə nömrəsi",max_length=30)
    message = models.TextField("Mesaj")
    status = models.BooleanField("Status", default=False)

    class Meta:
        ordering = ["-status", "-id"]
        verbose_name = "Mesaj"
        verbose_name_plural = lazy(lambda: _('Mesajlar ({})').format(Message.objects.filter(status=False).count()), str)()

    def ad(self):
        return mark_safe(f"<b>{self.name}</b>") if not self.status else mark_safe(f"{self.name}")
    
    def mail(self):
        return mark_safe(f"<b>{self.email}</b>") if not self.status else mark_safe(f"{self.email}")
    
    def telefon(self):
        return mark_safe(f"<b>{self.phone_number}</b>" if not self.status else mark_safe(f"{self.phone_number}"))

    def __str__(self):
        return self.name


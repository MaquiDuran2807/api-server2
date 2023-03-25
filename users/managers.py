from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager,models.Manager):
    def _create_user(self, username, email, password, is_staff , is_superuser,**extra_fields):
        if not username:
            raise ValueError('Los usuarios deben tener un nombre de usuario')

        if not email:
            raise ValueError('Los usuarios deben tener un correo electronico')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class TblUserManager(BaseUserManager):
    def create_user(self, name, email, password, invoice_id=None):
        if not name:
            raise ValueError("Name is required")
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")

        user = self.model(
            email = self.normalize_email(email),
            name = name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password):
        user = self.create_user(
            name = name,
            email = email,
            password = password
        )
        user.is_superuser = True
        user.save(using = self._db)
        return user


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["name"]

    objects = TblUserManager()

    def __str__(self):
        return self.email

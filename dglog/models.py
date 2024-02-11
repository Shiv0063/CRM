from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator

class Nuser(models.Model):
    mobile = models.CharField(max_length=20,null=True)
    status = models.IntegerField(default=0)

class UserManager(BaseUserManager):

    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError('Please provide a valid Phone')

        user = self.model(
            phone = phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, phone, password):
        user = self.create_user(
            phone,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password):
        user = self.create_user(
            phone,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):

    phone = models.CharField(max_length=15,unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
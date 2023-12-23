import uuid
from django.db import models
from .._bases.models.base import Person
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class ShmisUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email')
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth
            )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  password=None):
        user = self.create_user( 
            email=self.normalize_email(email),
            password=password,
            first_name=None,
            last_name=None,
            date_of_birth=None
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user
    

class ShmisUser(Person, AbstractBaseUser):
    class Meta:
        db_table='user'
    
    is_admin = models.BooleanField(default=False)
    is_school_admin =  models.BooleanField(default=False)
    is_school_parent =  models.BooleanField(default=False)
    is_school_nurse =  models.BooleanField(default=False)
    is_doctor =  models.BooleanField(default=False)

    is_active = models.BooleanField(default=False)

    #api_key = models.UUIDField(default=uuid.uuid4, unique=True)

    objects = ShmisUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

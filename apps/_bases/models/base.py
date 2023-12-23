from django.db import models
from django.utils.translation import gettext_lazy as _

class Base(models.Model):
    created = models.DateTimeField(null=True, auto_now_add=True) 
    updated = models.DateTimeField(null=True, auto_now=True) 

    class Meta:
        abstract = True


class Person(Base):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250, blank=True)
    date_of_birth = models.DateField(null=True)
    phone = models.CharField(max_length=15, blank=True)

    class Meta:
        abstract = True
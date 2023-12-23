from django.db import models
from django.utils.translation import gettext_lazy as _

GENDER=[("M", "Mâle"), ("F", "Femâle") ]

OWNERSHIP=[("GOV", "Governement"),("PRIV", "Private")]

class Base(models.Model):
    created = models.DateTimeField(null=True, auto_now_add=True) 
    updated = models.DateTimeField(null=True, auto_now=True) 

    class Meta:
        abstract = True
class Person(Base):
    first_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, default='M')
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=15, blank=True)

    

    class Meta:
        abstract = True
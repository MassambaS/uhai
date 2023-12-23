from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


GENDER=[("M", "Mâle"), ("F", "Femâle") ]
class Students(models.Model):
    """TODO: """
    class Meta:
        db_table = 'Students'
    
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, default='M')
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(null=True, blank=True)
    date_of_birth = models.DateField(null=True)
    created_at = models.DateField(null=True)
    update_at = models.DateField(null=True)

    father = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    mother = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')

    key = models.CharField(max_length=15, unique=True,blank=True)
from django.db import models
from ..accounts.models import ShmisUser
from .._bases.models.base import Person, Base, OWNERSHIP

class Country(models.Model):
    class Meta:
        db_table = "country"
    
    name = models.CharField(max_length=100)

class District(models.Model):
    class Meta:
        db_table = 'districts'

    REGIONS = [
        ("EAST", "Eastern regions"),
        ("WEST", "Western regions"),
        ("NORTH", "Northern regions"),
        ("SOUTH", "Southern regions"),
        ("CENTRAL", "Central regions"),
    ]
    
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.CharField(max_length=7, choices=REGIONS)

class County(models.Model):
    class Meta:
        db_table = 'counties'
    
    name = models.CharField(max_length=200)
    district= models.ForeignKey(District, on_delete=models.CASCADE)

class Sub_county(models.Model):
    class Meta:
        db_table = 'subCounties'
    
    name = models.CharField(max_length=200)
    county= models.ForeignKey(County, on_delete=models.CASCADE)

class Parish(models.Model):
    class Meta:
        db_table = 'parishes'
    
    name = models.CharField(max_length=200)
    sub_county= models.ForeignKey(Sub_county, on_delete=models.CASCADE)
    
class Village(models.Model):
    class Meta:
        db_table = 'villages'
    
    name = models.CharField(max_length=200)
    parish= models.ForeignKey(Parish, on_delete=models.CASCADE)


SCHOOL_YEAR=[(1, "First"),(2, "Second"),(3, "Third"),(4, "Fourth"),(5, "Fifth"),(6, "Sixth")]

SCHOOL_LEVELS = [("PRIMARY", "Primary school"),("SECONDARY", "Upper secondary")]

SCHOOL_TYPES=[("DAY", "Day"),("BOARDING", "Boarding"),("DAY_BOARDING", "Day & Boarding")]


class School(Base):
    class Meta:
        db_table = 'schools'
    
    name = models.CharField(max_length=200)
    badge = models.CharField(max_length=50)
    phone= models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    level = models.CharField(max_length=10, choices=SCHOOL_LEVELS)
    ownership = models.CharField(max_length=4, choices=OWNERSHIP)
    type = models.CharField(max_length=12, choices=SCHOOL_TYPES)

    village= models.ForeignKey(Village, on_delete=models.CASCADE)

class Students(Person):
    """TODO: """
    class Meta:
        db_table = 'students'
        
    father = models.ForeignKey(ShmisUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    mother = models.ForeignKey(ShmisUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    key = models.CharField(max_length=15, unique=True,blank=True)

class StudentSchoolHistory(Base):
    
    class Meta:
        db_table = 'students_school_history'
    
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')    
    student = models.ForeignKey(Students, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    
    level = models.CharField(max_length=10, choices=SCHOOL_LEVELS) 
    year = models.CharField(max_length=1, choices=SCHOOL_YEAR)

    success = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
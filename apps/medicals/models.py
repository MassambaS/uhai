from django.db import models
from .._bases.models.base import Base, OWNERSHIP
from ..schools.models import Students, Village
from ..accounts.models import ShmisUser


class Hospital(models.Model):
    """TODO: """
    class Meta:
        db_table = "hospitals"

       
    HOSPITAL_TYPES = [
        ("NRH", "National Referral Hospital"),
        ("RRH", "Regional Referral Hospital"),
        ("GH", "General Hospital"),
        ("HC_IV", "HC IV (County/Constituency)"),
        ("HC_III", "HC III (Sub county)"),
        ("HC_II", "HC II (Parish)"),
        ("VHT", "Village Health Team"),
    ]

    name = models.CharField(max_length=250)
    type = models.CharField(max_length=6, choices=HOSPITAL_TYPES)
    ownership = models.CharField(max_length=4, choices=OWNERSHIP)
    location =  models.ForeignKey(Village, on_delete=models.SET_NULL, null=True, blank=True)

class Examinations(Base):
    """TODO: """
    class Meta:
        db_table='examinations'

    symptomes = models.TextField(default='')
    comments = models.TextField(default='')
    student = models.ForeignKey(Students, on_delete=models.CASCADE)

class Devices(Base):
    """TODO:"""
    class Meta:
        abstract = True  

    why = models.ForeignKey(Examinations, on_delete=models.CASCADE)
    by = models.ForeignKey(ShmisUser, on_delete=models.SET_NULL, null=True, blank=True) 

class OximeteryTensiometer(Devices):
    """TODO: """
    class Meta:
        db_table='oximetry_tensiometer'
    
    DEVICES_TYPE = [("OXY", "Oxymetery"),("TEMP", "Thermometer")]

    value = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    type = models.CharField(max_length=4, choices=DEVICES_TYPE)

class BPM(Devices):
    """TODO: """
    class Meta:
        db_table='bpms'
    
    systole = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    diastole = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    pulse = models.DecimalField(max_digits=5, decimal_places=2, blank=True)

class BMI(Devices):
    """TODO: """
    class Meta:
        db_table='bmis'

    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    bmi = models.DecimalField(max_digits=5, decimal_places=2, blank=True)

class Prescriptions(Base):
    """TODO: """
    class Meta:
        db_table='prescriptions'

    examinations = models.ForeignKey(Examinations, on_delete=models.CASCADE)
    by = models.ForeignKey(ShmisUser, on_delete=models.CASCADE)

class MedicalLeave(Base):    
    """TODO: """
    class Meta:
        db_table='medical_leaves'

    comments = models.TextField(default='')
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)

    prescription = models.ForeignKey(Prescriptions, on_delete=models.CASCADE)

class Drugs(Base):
    """TODO: """
    class Meta:
        db_table = 'drugs'
    
    name = models.CharField(max_length=255)

class DrugsPrescripted(Base):
    """TODO: """   
    class Meta:
        db_table='drugs_prescriptions'
    
    MEDICATION_TIMES=[
        ("MO","Morning only"),
        ("NO","Noon Only"),
        ("NI","Night Only"),
        ("MO_NO","Morning & Noon"),
        ("MO_NI","Morning & Night"),
        ("NO_NI","Morning & Night"),
        ("MO_NO_NI","Morning, Noon & Night")
    ]


    comments = models.TextField()
    drug = models.ForeignKey(Drugs, on_delete=models.CASCADE)
    taking_number = models.IntegerField(default=1)
    taking_interval = models.CharField(max_length=8,choices=MEDICATION_TIMES)
    renew = models.BooleanField(default=False)

    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    
    prescription = models.ForeignKey(Prescriptions, on_delete=models.CASCADE)
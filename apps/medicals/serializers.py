from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *

DEFAULT_READ_ONLY_FIELDS = ['created', 'updated']
class OxyTenSerializer(serializers.ModelSerializer):

    def create(self, validated_data, device_type):
        
        d_type = 'OXY' if device_type.lower() == 'oxy' else "TEMP" if device_type.lower() == 'temp' else ''

        if d_type == '':
            raise ValidationError("Unknown device type: {device_type}")
        
        device = OximeteryTensiometer(
            value=validated_data['value'],
            type=d_type
        ) 

        device.save()

        return device

    
    def update(self, validated_data):
        device = OximeteryTensiometer( value=validated_data['value'] ) 
        device.save()
        return device
        
    class Meta:
        model: OximeteryTensiometer
        fields = ['value', 'why', 'by']
        read_only_fields = DEFAULT_READ_ONLY_FIELDS
class BMISerializer(serializers.ModelSerializer):

    def create(self, validated_data, formula=True):
        bmi_result = round((validated_data['weight']/(validated_data['height'] ** 2)), 2)

        bmi = BMI(
            weight=validated_data['weight'],
            height=validated_data['height'],
            bmi=validated_data['bmi'] if not formula else bmi_result
        ) 

        bmi.save()

        return bmi

    def update(self, validated_data, formula):
        self.create(validated_data=validated_data, formula=formula)
        
    class Meta:
        model: BMI
        fields = ['weight', 'height', 'bmi', 'why', 'by']
        read_only_fields = DEFAULT_READ_ONLY_FIELDS

class BPMSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        bpm = BPM(
            systole=validated_data['systole'],
            diastole=validated_data['diastole'],
            pulse=validated_data['pulse']
        ) 

        bpm.save()

        return bpm

    def update(self, validated_data):
        self.create(validated_data=validated_data)
        
    class Meta:
        model: BPM
        fields = ['systole', 'diastole', 'pulse', 'why', 'by']
        read_only_fields = DEFAULT_READ_ONLY_FIELDS

class ExaminationsSerialier(serializers.ModelSerializer):

    def create(self, validated_data):
        pass
    
    def update(self, validated_data):
        pass

    class Meta:
        model: Examinations
        fields = ['systole', 'diastole', 'pulse']
        read_only_fields = DEFAULT_READ_ONLY_FIELDS

class HospitalSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        pass
    
    def update(self, validated_data):
        pass

    

    class Meta:
        model: Hospital

class MedicalLeaveSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        pass
    
    def update(self, validated_data):
        pass

    class Meta:
        model: MedicalLeave

class DrugsPrescriptionsSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        pass
    
    def update(self, validated_data):
        pass

    class Meta:
        model: DrugsPrescriptions
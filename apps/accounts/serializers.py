from .models import ShmisUser
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError


DEFAULT_READ_ONLY_FIELDS = ['created', 'updated', 'last_login']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = ShmisUser
        fields = '__all__'
        read_only_fields = DEFAULT_READ_ONLY_FIELDS
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
        }



class AuthSerializer(serializers.Serializer):
    """serializer for the user authentication object"""
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )  

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        user = authenticate(
            request=self.context.get('request'),
            email=email,
            password=password
        )
        
        if not user:
            msg = ('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return 
    

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        if ShmisUser.objects.filter(email=validated_data['email']):
            raise ValidationError("Email already used")
        
        user = ShmisUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            date_of_birth=validated_data['date_of_birth']
        )
        
        return user


    class Meta:
        model = ShmisUser
        fields = '__all__'
        read_only_fields = DEFAULT_READ_ONLY_FIELDS
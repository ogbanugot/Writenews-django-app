from .models import User 
from django.core.validators import RegexValidator
from rest_framework import serializers

class LoginSerializer(serializers.ModelSerializer):
    #This takes precedencer over the extra_kwargs
    email = serializers.EmailField(max_length=150, help_text = "Required. Enter a valid email address")
    class Meta:
        model = User
        fields = ('email','password')

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=150, help_text = "Required. Enter a valid email address")
    password = serializers.CharField(max_length=128)
    class Meta:
        model = User
        fields = ('name','bio','email','password')


    
        

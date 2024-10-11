from rest_framework import serializers
from .models import User, UserManager

class UserSerialize(serializers.ModelSerializer):
    # To hide the password in the response when creating or retrieving a user
    password = serializers.CharField(write_only=True)

    class Meta:
        model= User
        fields=['id','username','email','birthday', 'password']

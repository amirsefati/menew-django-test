from rest_framework import serializers
from .models import User, UserManager

class UserSerialize(serializers.ModelSerializer):
    
    # To hide the password in the response when creating or retrieving a user
    password = serializers.CharField(write_only=True)

    class Meta:
        model= User
        fields=['id','username','email','birthday', 'password']

        def create(self, validated_data):
            email = validated_data.get('email')
            password = validated_data.get('password')
            user = UserManager.create_user(email, password , validated_data)
            return user

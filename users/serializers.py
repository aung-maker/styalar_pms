from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'mobile_number', 'address', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        # By default, we set is_active=False so an Admin must approve the 'Request'
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            mobile_number=validated_data.get('mobile_number', ''),
            address=validated_data.get('address', ''),
            is_active=False  
        )
        return user
    
class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']
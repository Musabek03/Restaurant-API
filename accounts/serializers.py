from rest_framework import serializers
from .models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password_confirm = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ['id', 'phone_number', 'email', 'full_name','password', 'password_confirm']
    
    def validate(self,attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({
                "error": "Parollar saykes emes,tekserip qaytadan jazin"
            })
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')

        user = CustomUser.objects.create(
            phone_number = validated_data['phone_number'],
            email = validated_data['email'],
            full_name = validated_data['full_name'],
            role = 'customer',
            is_active = True
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'phone_number', 'full_name','role', 'created_at']
        read_only_fields = ['role', 'created_at']
        

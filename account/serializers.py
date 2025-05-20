from rest_framework import serializers
from .models import CustomUser  # Import your custom user model
from .models import OTPVerification
from django.contrib.auth import get_user_model

User = get_user_model()

class OTPRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    purpose = serializers.ChoiceField(choices=OTPVerification.PURPOSE_CHOICES)

class OTPVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile_pic_url = serializers.SerializerMethodField()  # Add this line

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'profile_photo', 'password', 'profile_pic_url']  # Include profile_pic_url here

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
    
    def get_profile_pic_url(self, obj):
        request = self.context.get('request')
        if obj.profile_photo and hasattr(obj.profile_photo, 'url'):
            return request.build_absolute_uri(obj.profile_photo.url)  # Return the full URL to the image
        return None
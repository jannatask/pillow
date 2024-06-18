from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'full_name', 'email', 'phone_number']




from django.contrib.auth import get_user_model

# from .utils import send_activation_code

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length = 4, required=True, write_only=True)
    password_confirm = serializers.CharField(min_length = 4, required=True, write_only=True)
    
    class Meta:
        model = User
        fields = 'email', 'password', 'password_confirm'

    def validate(self, attrs):
        pswd = attrs.get('password')
        cnfrm = attrs.pop('password_confirm')

        if pswd != cnfrm:
            raise serializers.ValidationError('Пароли не совпали')
        return attrs
    
#     def create(user, validated_data):
#         user = User.objects.create_user(**validated_data)
#         send_activation_code.delay(user.email, user.activation_code)
#         return user
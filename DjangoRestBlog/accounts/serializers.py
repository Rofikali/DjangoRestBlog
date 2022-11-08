import email
from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        max_length=100,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'tc']
        extra_kwargs = {'password': {'write_only': True}}

    # We are writing this becoz we need confirm password field in our Registratin Request

    def validate(self, data):
        """
        Check that all data valid or not before finish.
        """
        password1 = data.get('password')
        password2 = data.get('password2')

        if password1 != password2:
            raise serializers.ValidationError(
                "Password and Password2 does not match.")
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

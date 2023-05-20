from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6, max_length=128)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    
class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    # role = serializers.SlugRelatedField(slug_field='role', queryset=Role.objects.exclude(role='admin').all())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        # extra_kwargs = {
        #     'username': {'required': True},
        #     'email': {'required': True},
        #     'password': {'required': True},
        #     'password2': {'required': True}
        # }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user

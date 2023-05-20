from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from .models import User


# User model
class CreateReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'role']


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'email', 'role']

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value






# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, min_length=6, max_length=128)

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'role', 'password')

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user
    
    
class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'role', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'], role=validated_data['role'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_new_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['old_password', 'new_password', 'confirm_new_password']

    def validate(self, attrs):
        new_password = attrs.get('new_password')
        confirm_password = attrs.get('confirm_new_password')

        if new_password and confirm_password and new_password != confirm_password:
            raise serializers.ValidationError({"New password": "Password fields didn't match."})
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is not correct") 
        return value

    # def update(self, instance, validated_data):
    #     user = self.context['request'].user

    #     if not (user.is_staff or user.pk == instance.pk):
    #         raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

    #     instance.set_password(validated_data['new_password'])
    #     instance.save()
    #     return instance
    
    def save(self):
        user = self.context['request'].user
        new_password = self.validated_data['new_password']
        user.set_password(new_password)
        user.save()
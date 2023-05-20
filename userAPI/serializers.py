from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from userAPI.models import User

class BaseUserSerializer(serializers.ModelSerializer):

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value
    
    
class RetrieveUpdateDestroyUserSerializer(BaseUserSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'role']
        
    def get_fields(self):
        fields = super().get_fields()
        fields['role'].read_only = True 
        return fields


class AdminRetrieveUpdateDestroyUserSerializer(BaseUserSerializer):
    # email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'role']

    
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

    def get_fields(self):
        fields = super().get_fields()
        user = self.context['request'].user

        # Exclude 'admin' option for anonymous users
        if not user.is_authenticated:
            fields['role'].choices = [choice for choice in User.ROLE_CHOICES if choice[0] != 'admin']

        return fields
    
    
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
    
    def save(self):
        user = self.context['request'].user
        new_password = self.validated_data['new_password']
        user.set_password(new_password)
        user.save()
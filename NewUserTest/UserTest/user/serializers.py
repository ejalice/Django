from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = "__all__"
    
    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User(
            email=email
        )
        user.set_password(password)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
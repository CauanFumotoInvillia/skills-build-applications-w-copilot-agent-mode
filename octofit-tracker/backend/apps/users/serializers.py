from rest_framework import serializers
from .models import User, Profile  # Assuming the User model is defined in models.py


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    # serialize the team's ObjectId as a string to avoid JSON encoding errors
    team = serializers.CharField(source='team._id', read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'team']


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'team']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        Profile.objects.create(user=user)
        return user
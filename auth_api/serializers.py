from rest_framework import serializers
from .models import User

from django.contrib.auth.hashers import make_password, check_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')

    def create(self, validated_data):
        user = User.objects.create(
        username=validated_data['username'],
        password = make_password(validated_data['password'])
        )
        user.save()
        # user will need to be modified here to remove the hashed password
        return user

    def update(self, instance, validated_data):
        user = User.objects.get(username=validated_data['username'])
        user.password = make_password(validated_data['password'])
        user.save()
        # user will need to be modified here to remove the hashed password
        return user

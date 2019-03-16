
# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('id', 'email', 'username', 'password', 'names', 'surnames', 'phone', 'gender')

    read_only_fields = ('is_staff', 'created_at', 'updated_at')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super(UserSerializer, self).update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        extra_kwargs = {'provider_id': {'write_only': True}}
        fields = ('id', 'names', 'surnames', 'birthday', 'gender', 'phone',
                  'email', 'picture', 'location', 'category', 'skill', 'created_at', 'updated_at', 'last_login')

    read_only_fields = ('created_at', 'updated_at', 'last_login')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        # user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super(UserSerializer, self).update(instance, validated_data)
        # update if is necesary add user with form from the frontend
        # user.set_password(validated_data['password'])
        user.save()
        return user

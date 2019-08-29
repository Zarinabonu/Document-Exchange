from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from user.models import Profile
from django.contrib.auth.models import User


class User_Serializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


    def create(self, validated_data):
        u = User(**validated_data)
        print(u.password)

        u.set_password(u.password)

        u.save()
        print(u.password)
        return u




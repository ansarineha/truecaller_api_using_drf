from rest_framework import serializers
from .models import Contact,MapUserContact,Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class MapUserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


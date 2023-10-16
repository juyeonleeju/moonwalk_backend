# serializers.py
from rest_framework import serializers
from .models import Runningmate

class RunningmateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Runningmate
        fields = '__all__'
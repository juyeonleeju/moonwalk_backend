from rest_framework import serializers
from django.contrib.auth import collections

class collectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = collections()
        fields = '__all__'
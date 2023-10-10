from rest_framework import serializers
from .models import Runrecord

class RunrecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Runrecord
        fields = ['walk_count'] #왜 walk_count 만 하는진 모름
from django.core import serializers
from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer): #모델 인스턴스에서 id를 제외한 모든 field의 값을 직렬화하라는 역할을 가진 클래스
    class Meta:
        model = Course
        fields = '__all__'
        

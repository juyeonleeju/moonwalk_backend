from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Course
from .serializers import CourseSerializer
from django.http import HttpResponse
import pandas as pd


def course_list(request):
    if request.method == 'GET':
        query_set = Course.objects.all()
        serializer = CourseSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    return HttpResponse('Course')


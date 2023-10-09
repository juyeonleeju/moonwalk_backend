from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Runrecord
from .serializers import RunrecordSerializer 
from rest_framework.parsers import JSONParser
# Create your views here.

#runrecord 
#누적 걸음걸이 수 put 해주기

def Runrecord(request): 
    if request.method == 'GET':
            query_set = Runrecord.objects.all()
            serializer = RunrecordSerializer(query_set, many=True)
            return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        total_walk_count = walk_count.

        sum = 
        data = JSONParser().parse(request)
        serializer = RunrecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


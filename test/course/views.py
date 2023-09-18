import json
from django.views import View
from .models import Runningmate
from django.http import HttpResponse   #.response
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

def course_list(request, pk):
    ESNTL_ID = get_object_or_404(ESNTL_ID, pk=pk)
    if request.method == 'PUT':
        # 특정 글 갱신을 구현
        put_data = Runningmate(request.body)
        form = Runningmate(put_data, instance=post)
        if form.is_valid():
            post = form.save()
            return JsonResponse(post)
        return JsonResponse(form.errors)
    
    elif request.method == 'DELETE':
        # 특정 글 삭제를 구현
        post.delete()
        return HttpResponse()
    
    else:
        # 특정 글 내용 응답을 구현
        return JsonResponse(post)



def index(request):
    context = {
        'message': 'Hello, Django!'
    }
    return render(request, 'index.html', context)









"""
def course_list(request):
    if request.method == 'GET': #겟 #httpresponse
        query_set = Course.objects.all()
        serializer = CourseSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST': #포스트 #httpresponse
        data = JSONParser().parse(request)
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    return HttpResponse('Course')
"""

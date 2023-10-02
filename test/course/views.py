import json
from django.views import View
from .models import Runningmate
from django.http import HttpResponse   #.response
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Runningmate

# Runningmate 정보를 반환하는 클래스 정의

class RunningmateView(View):
    def get(self, request, *args, **kwargs): # 요청에서 Rm_id와 Rm_Name 매개변수를 가져옵니다.
      Rm_id = request.GET.get('Rm_id', None)
      Rm_Name = request.GET.get('Rm_Name', None)
    
      Rm_id = Rm_id.objects.get(id=Rm_id)
    
      Runnungmate_information = {
        "Rm_id": Rm_id,
        "Rm_Name": Rm_Name
     }.save()
    
      return JsonResponse({"message": Runnungmate_information}, status=200)


def Rm_list(request, pk):
    ESNTL_ID = get_object_or_404(ESNTL_ID, pk=pk)
    if request.method == 'PUT':
        # 특정 글 갱신을 구현
        put_data = Runningmate(request.body)
        form = Runningmate(put_data, instance=post)
        if form.is_valid():
            post = form.save()
            return JsonResponse(post)
        return JsonResponse(form.errors)
    
    
    else:
        # 특정 글 내용 응답을 구현
        return JsonResponse(post)
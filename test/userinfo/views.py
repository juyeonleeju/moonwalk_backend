import json
from django.views import View
from .models import userinformation
from django.http import HttpResponse   #.response
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404


# Runningmate 정보를 반환하는 클래스 정의

class userinformationView(View):
    def get(self, request, *args, **kwargs): # 요청에서 Rm_id와 Rm_Name 매개변수를 가져옵니다.
      nickname = request.GET.get('nickname', None)
      goal = request.GET.get('goal', None)
    
      nickname = nickname.objects.get(id=nickname)
    
      userinformation = {
        "nickname": nickname,
        "goal": goal
     }.save()
    
      return JsonResponse({"message": userinformation}, status=200)


def userinformation_list(request, pk):
    ESNTL_ID = get_object_or_404(ESNTL_ID, pk=pk)
    if request.method == 'PUT':
        # 특정 글 갱신을 구현
        put_data = userinformation(request.body)
        form = userinformation(put_data, instance=post)
        if form.is_valid():
            post = form.save()
            return JsonResponse(post)
        return JsonResponse(form.errors)
    
    
    else:
        # 특정 글 내용 응답을 구현
        return JsonResponse(post)
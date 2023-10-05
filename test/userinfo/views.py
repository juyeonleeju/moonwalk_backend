
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

from django.shortcuts import render
import json
from django.views import View
from django.http import JsonResponse
from .models import userinfo

class User_info(View):
    def post(self, request):
        data = json.loads(request.body)
        User_info(
            User_ID = data['name'],
            goal = data['goal'],
            User_lev  = data['User_lev'],
            img  = data['img'],
            attendance  = data['attendance'],
        ).save()						# 받아온 데이터를 DB에 저장시켜줌

        return JsonResponse({'message':''},status=200)


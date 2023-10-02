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

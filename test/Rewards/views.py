
# Create your views here.
from django.shortcuts import render
import json
from django.views import View
from django.http import JsonResponse
from .models import Rewards

class reward_View(View):
    def post(self, request):
        data = json.loads(request.body)
        Rewards(
            xp    = data['xp']+1,
            COURS_LEVEL = data[' COURS_LEVEL']
        ).save()						# 받아온 데이터를 DB에 저장시켜줌

        return JsonResponse({'message':'레벨업 완료><'},status=200)
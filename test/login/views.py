
import json
from django.views import View
from django.http import JsonResponse
from .models import Account # 가정: Account 모델이 애플리케이션에서 정의되어 있다고 가정
# 사용자 회원가입을 처리하는 클래스를 정의
class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        Account(
            User_ID    = data['User_ID'],
            password = data['password']
        ).save()						# 받아온 데이터를 DB에 저장시켜줌

        return JsonResponse({'message':'회원가입 완료'},status=200)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        if Account.objects.filter(email = data['email']).exists() :
            user = Account.objects.get(email = data['email'])
            if user.password == data['password'] :
                return JsonResponse({'message':f'{user.email}님 로그인 성공!'}, status=200)
            else :
                return JsonResponse({'message':'비밀번호가 틀렸어요'},status = 200)

        return JsonResponse({'message':'등록되지 않은 이메일 입니다.'},status=200)
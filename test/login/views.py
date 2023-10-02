
import json
from django.views import View
from django.http import JsonResponse
from .models import Account_info
from .models import Account # 가정: Account 모델이 애플리케이션에서 정의되어 있다고 가정
# 사용자 회원가입을 처리하는 클래스를 정의
class SignUpView(View):
    def post(self, request): # 요청의 body에서 JSON 데이터를 파싱
        data = json.loads(request.body)
        Account( # 새로운 Account 인스턴스를 생성하고 데이터베이스에 저장
            email    = data['email'],
            password = data['password'],
            User_ID = data['User_ID'],
            name = data['name'],
            phone = data['phone'],
            created_at = data['created_at'],
            updated_at = data['updated_at'],
        ).save()						# 받아온 데이터를 DB에 저장시켜줌
# 회원가입이 완료되었다는 메시지를 포함한 JSON 응답을 반환
        return JsonResponse({'message':'회원가입 완료'},status=200)
# 사용자 로그인을 처리하는 클래스를 정의
class SignInView(View):
    def post(self, request): # 요청의 본문에서 JSON 데이터를 파싱
        data = json.loads(request.body)
# 제공된 이메일로 등록된 계정이 데이터베이스에 존재하는지 확인
        if Account.objects.filter(email = data['email']).exists() :
            user = Account.objects.get(email = data['email'])
            # 제공된 비밀번호가 저장된 비밀번호와 일치하는지 확인
            if user.password == data['password'] :
                return JsonResponse({'message':f'{user.email}님 로그인 성공!'}, status=200)
            else :
                return JsonResponse({'message':'비밀번호가 틀렸어요'},status = 200)

        return JsonResponse({'message':'등록되지 않은 이메일 입니다.'},status=200)
 
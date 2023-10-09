from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

from login.serializers import UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    user_ID = request.data.get('user_ID')
    email = request.data.get('email')
    password = request.data.get('password')
    name = request.data.get('name')

    serializer = UserSerializer(data=request.data)
    serializer.email = email
    serializer.name = name
    serializer.user_ID = user_ID

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(password)
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    user_ID = request.data.get('user_ID')
    #email = request.data.get('email')
    password = request.data.get('password')

    #로그인 오류
    user = authenticate(user_ID=user_ID, password=password)
    if user is None: 
        return Response({'message': '아이디 또는 비밀번호가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

    #토큰화
    refresh = RefreshToken.for_user(user)
    update_last_login(None, user)

    return Response({'refresh_token': str(refresh),
                     'access_token': str(refresh.access_token), }, status=status.HTTP_200_OK)





# import json
# from django.views import View
# from django.http import JsonResponse
# from .models import Account # 가정: Account 모델이 애플리케이션에서 정의되어 있다고 가정
# # 사용자 회원가입을 처리하는 클래스를 정의
# class SignUpView(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         Account(
#             User_ID    = data['User_ID'],
#             password = data['password']
#         ).save()						# 받아온 데이터를 DB에 저장시켜줌

#         return JsonResponse({'message':'회원가입 완료'},status=200)

# class SignInView(View):
#     def post(self, request):
#         data = json.loads(request.body)

#         if Account.objects.filter(email = data['email']).exists() :
#             user = Account.objects.get(email = data['email'])
#             if user.password == data['password'] :
#                 return JsonResponse({'message':f'{user.email}님 로그인 성공!'}, status=200)
#             else :
#                 return JsonResponse({'message':'비밀번호가 틀렸어요'},status = 200)

#         return JsonResponse({'message':'등록되지 않은 이메일 입니다.'},status=200)
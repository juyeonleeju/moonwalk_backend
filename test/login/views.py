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
def signup(request): # POST 요청으로부터 사용자 등록 정보(user_ID, email, password, name)를 가져옵니다.
    user_ID = request.data.get('user_ID')
    email = request.data.get('email')
    password = request.data.get('password')
    name = request.data.get('name')
 # UserSerializer를 사용하여 요청 데이터를 직렬화합니다.
    serializer = UserSerializer(data=request.data)
    serializer.email = email# 직렬화한 데이터에 사용자 정보를 추가
    serializer.name = name
    serializer.user_ID = user_ID
 # 데이터가 유효한지 확인합니다. 데이터가 유효하지 않으면 예외를 발생시킵니다.
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(password)
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request): # POST 요청으로부터 사용자 로그인 정보(user_ID, password)를 가져옵니다.
    user_ID = request.data.get('user_ID') # 사용자 인증을 시도
    #email = request.data.get('email')
    password = request.data.get('password')

    #로그인 오류 #  # 인증 실패 시 에러 응답을 반환
    user = authenticate(user_ID=user_ID, password=password)
    if user is None: 
        return Response({'message': '아이디 또는 비밀번호가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

    #토큰화
    refresh = RefreshToken.for_user(user) ## 새로운 액세스 토큰 및 리프레시 토큰을 생성
    update_last_login(None, user) ## 사용자의 로그인 시간을 업데이트
 # 성공적인 응답을 반환
    return Response({'refresh_token': str(refresh),
                     'access_token': str(refresh.access_token), }, status=status.HTTP_200_OK)






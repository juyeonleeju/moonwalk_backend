from django.urls import path
from . import views

urlpatterns = [
    # 객체 나열하고 새로운 객체 만들기
    path('your-models/', views.YourModelAPIView.as_view(), name='your-model-list'),

    # /your-models/1/과 같은 URL에 YourModelDetailAPIView를 매핑합니다. 여기서 1은 객체의 주요 키입니다.
    # 이 패턴은 개별 객체의 세부 정보, 업데이트 및 삭제를 처리
    path('your-models/<int:pk>/', views.YourModelDetailAPIView.as_view(), name='your-model-detail'),
]
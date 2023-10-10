from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Runrecord
from .serializers import RunrecordSerializer

class RunrecordView(APIView):
    def post(self, request):
        # POST 요청으로부터 walk_count 값을 가져옵니다.
        walk_count = request.data.get('walk_count')
        
        try:
            # 가장 최근의 레코드를 'updated_at' 필드를 기준으로 가져옵니다.
            latest_record = Runrecord.objects.latest('updated_at')
            previous_total_wc = latest_record.total_wc
        except Runrecord.DoesNotExist:
            # 이전 레코드가 없는 경우 0으로 초기화합니다.
            previous_total_wc = 0 
        
        # 새로운 total_wc 값을 계산합니다.
        total_wc = walk_count + previous_total_wc

        # RunrecordSerializer를 사용하여 새로운 레코드를 생성하고 데이터베이스에 저장합니다.
        serializer = RunrecordSerializer(data={'walk_count': walk_count, 'total_wc': total_wc})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # 직렬화 오류인 경우 에러 응답을 반환합니다.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Runningmate
from .serializers import RunningmateSerializer


class RandomRunningmateView(APIView):
    def get(self, request):
        # 랜덤하게 레코드 하나를 선택
        random_runningmate = Runningmate.objects.order_by('?').first()

        if random_runningmate:
            serializer = RunningmateSerializer(random_runningmate)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'No runningmate records found.'}, status=status.HTTP_NOT_FOUND)




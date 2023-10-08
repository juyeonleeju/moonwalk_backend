from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import userinformation
from userinfo.serializers import UserinfoSerializer

#모든 객체에 대한 GET(목록) 및 POST(생성) 작업을 처리
class YourModelAPIView(APIView):
    def get(self, request, format=None):
        # 데이터베이스에서 YourModel의 모든 객체를 검색합니다.
        queryset = userinformation.objects.all()
        serializer = UserinfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # 직렬화기를 사용하여 요청 데이터를 역직렬화합니다.
        serializer = UserinfoSerializer(data=request.data)
        if serializer.is_valid():
            # 새 객체를 데이터베이스에 저장합니다.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#주요 키 (pk)를 기반으로 모델의 단일 객체에 대한 GET(조회), PUT(수정) 및 DELETE(삭제) 작업을 처리
class YourModelDetailAPIView(APIView):
    def get_object(self, pk):
        # 주요 키 (pk)를 기반으로 YourModel의 단일 객체를 검색합니다.
        try:
            return userinformation.objects.get(pk=pk)
        except userinformation.DoesNotExist:
            raise Response(
                {"error": f"YourModel with id {pk} does not exist."},
                status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        # 단일 객체를 검색하고 직렬화합니다.
        your_model_instance = self.get_object(pk)
        serializer = UserinfoSerializer(your_model_instance)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        # 단일 객체를 검색하고 요청 데이터를 기반으로 업데이트합니다.
        your_model_instance = self.get_object(pk)
        serializer = UserinfoSerializer(your_model_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        # 단일 객체를 검색하고 삭제합니다.
        your_model_instance = self.get_object(pk)
        your_model_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# import json
# from django.views import View
# from .models import userinformation
# from django.http import HttpResponse   #.response
# from django.http import JsonResponse
# from django.shortcuts import render, get_object_or_404


# # Runningmate 정보를 반환하는 클래스 정의

# class userinformationView(View):
#     def get(self, request, *args, **kwargs): # 요청에서 Rm_id와 Rm_Name 매개변수를 가져옵니다.
#       nickname = request.GET.get('nickname', None)
#       goal = request.GET.get('goal', None)
    
#       nickname = nickname.objects.get(id=nickname)
    
#       userinformation = {
#         "nickname": nickname,
#         "goal": goal
#      }.save()
    
#       return JsonResponse({"message": userinformation}, status=200)


# def userinformation_list(request, pk):
#     ESNTL_ID = get_object_or_404(ESNTL_ID, pk=pk)
#     if request.method == 'PUT':
#         # 특정 글 갱신을 구현
#         put_data = userinformation(request.body)
#         form = userinformation(put_data, instance=post)
#         if form.is_valid():
#             post = form.save()
#             return JsonResponse(post)
#         return JsonResponse(form.errors)
    
    
#     else:
#         # 특정 글 내용 응답을 구현
#         return JsonResponse(post)
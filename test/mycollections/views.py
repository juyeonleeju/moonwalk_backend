from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import collections
from userinfo.serializers import collectionsSerializer

class collectionsAPIView(APIView):
    def get(self, request, format=None):
        # 데이터베이스에서 YourModel의 모든 객체를 검색합니다.
        queryset = collections.objects.all()
        serializer = collectionsSerializer(queryset, many=True)
        return Response(serializer.data)

class cRm_listAPIView(APIView):
    def get_object(self, pk):
        # 주요 키 (pk)를 기반으로 YourModel의 단일 객체를 검색합니다.
        try:
            return collections.objects.get(pk=pk)
        except collections.DoesNotExist:
            raise Response(
                {"error": f"YourModel with id {pk} does not exist."},
                status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, format=None):
        # 단일 객체를 검색하고 요청 데이터를 기반으로 업데이트합니다.
        your_model_instance = self.get_object(pk)
        serializer = collectionsSerializer(your_model_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# import json
# from django.views import View
# from .models import collections
# from django.http import HttpResponse   #.response
# from django.http import JsonResponse
# from django.shortcuts import render, get_object_or_404

# # Create your views here.
# class collectionsView(View):
#     def get(self, request, *args, **kwargs): # 요청에서 Rm_id와 Rm_Name 매개변수를 가져옵니다.
#       cRm_id = request.GET.get('cRm_id', None)
#       cRm_Name = request.GET.get('cRm_Name', None)
    
#       cRm_id = cRm_id.objects.get(id=cRm_id)
    
#       my_collections = {
#         "cRm_id": cRm_id,
#         "cRm_Name": cRm_Name
#      }.save()
    
#       return JsonResponse({"message": my_collections}, status=200)

# def cRm_list(request, pk):
#     ESNTL_ID = get_object_or_404(ESNTL_ID, pk=pk)
#     if request.method == 'PUT':
#         # 특정 글 갱신을 구현
#         put_data = collections(request.body)
#         form = collections(put_data, instance=post)
#         if form.is_valid():
#             post = form.save()
#             return JsonResponse(post)
#         return JsonResponse(form.errors)
    
    
#     else:
#         # 특정 글 내용 응답을 구현
#         return JsonResponse(post)
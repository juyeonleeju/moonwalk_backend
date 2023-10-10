import json
from django.views import View
from .models import collections
from django.http import HttpResponse   #.response
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.
class collectionsView(View):
    def get(self, request, *args, **kwargs): # 요청에서 Rm_id와 Rm_Name 매개변수를 가져옵니다.
      cRm_id = request.GET.get('cRm_id', None)
      cRm_Name = request.GET.get('cRm_Name', None)
    
      cRm_id = cRm_id.objects.get(id=cRm_id)
    
      my_collections = {
        "cRm_id": cRm_id,
        "cRm_Name": cRm_Name
     }.save()
    
      return JsonResponse({"message": my_collections}, status=200)


def cRm_list(request, pk):
    ESNTL_ID = get_object_or_404(ESNTL_ID, pk=pk)
    if request.method == 'PUT':
        # 특정 글 갱신을 구현
        put_data = collections(request.body)
        form = collections(put_data, instance=post)
        if form.is_valid():
            post = form.save()
            return JsonResponse(post)
        return JsonResponse(form.errors)
    
    
    else:
        # 특정 글 내용 응답을 구현
        return JsonResponse(post)
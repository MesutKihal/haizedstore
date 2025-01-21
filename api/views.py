from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt 
from django.http import JsonResponse
from .models import Request

@csrf_exempt
def content(request, page):
    data = [[], [], []]
    if page == 'forms':
        pass
    elif page == 'requests':
        pass
    return JsonResponse(data, safe=False)

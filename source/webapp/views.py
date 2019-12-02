import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


@csrf_exempt
def api_add(request):
    result = None
    if request.body:
        request_data = json.loads(request.body)
        A = request_data['A']
        B = request_data['B']
        try:
            a = int(A)
            b = int(B)
            result = A + B
            data = {
                'Result': result
            }
            return JsonResponse(data)
        except:
            raise HttpResponseBadRequest



@csrf_exempt
def api_subtract(request):
    result = None
    if request.body:
        request_data = json.loads(request.body)
        A = request_data['A']
        B = request_data['B']
        try:
            a = int(A)
            b = int(B)
            result = A - B
            data = {
                'result': result
            }
            return JsonResponse(data)
        except:
            raise HttpResponseBadRequest

@csrf_exempt
def api_multiply(request):
    result = None
    if request.body:
        request_data = json.loads(request.body)
        A = request_data['A']
        B = request_data['B']
        try:
            a = int(A)
            b = int(B)
            result = A * B
            data = {
                'result': result
            }
            return JsonResponse(data)
        except:
            raise HttpResponseBadRequest

@csrf_exempt
def api_divide(request):
    result = None
    if request.body:
        request_data = json.loads(request.body)
        A = request_data['A']
        B = request_data['B']
        try:
            a = int(A)
            b = int(B)
            result = A / B
            data = {
                'result': result
            }
            return JsonResponse(data)
        except:
            raise HttpResponseBadRequest
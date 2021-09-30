from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name':'john',
            'age': 23
        }
        return Response(data)


# def test_view(request):
#     data = {
#         'name':'john',
#         'age': 23
#     }
#     return JsonResponse(data)
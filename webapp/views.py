from django.shortcuts import render
# use restframeworks
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#import models
from .models import employes
from .serializer import employeSerializer

class employlist(APIView):
    def get(self,request):
        employes1=employes.objects.all()
        serializer=employeSerializer(employes1,many=True)
        return Response(serializer.data)
        
    def post(self):
        pass
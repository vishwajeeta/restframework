from rest_framework import serializers
from .models import employes

class employeSerializer(serializers.ModelSerializer):
    class Meta:
        model=employes
        #fields=('firstname','lastname')          or
        fields='__all__'

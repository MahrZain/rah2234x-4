from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import serializers
from data.models import CustomUser

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
from rest_framework.views import APIView
from rest_framework import serializers
from .models import Office


class OfficeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    company_name = serializers.CharField()
    email = serializers.EmailField()
    company_code = serializers.CharField()
    strength = serializers.IntegerField()
    web_site = serializers.CharField()
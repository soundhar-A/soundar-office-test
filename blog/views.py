from django.shortcuts import render
from .serializers import OfficeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Office

# Create your views here.

class OfficeAPIView(APIView):
    serializer_class = OfficeSerializer
    def get(self,request):
        office = Office.objects.all().values()
        return Response({'Message':'List of Office','Office':office})
    def post(self,request):
        print('request data is:',request.data)
        serializer_obj = OfficeSerializer(data=request.data)
        if (serializer_obj.is_valid()):
            Office.objects.create(id = serializer_obj.data.get("id"),
                                 company_name = serializer_obj.data.get("company_name"),
                                 email = serializer_obj.data.get("email"),
                                 company_code = serializer_obj.data.get("company_code"),
                                 strength = serializer_obj.data.get("strength"),
                                 web_site = serializer_obj.data.get("web_site")


            )
            office = Office.objects.all().filter(id = request.data["id"])
        return Response({"message":"New office datails","Office":office})


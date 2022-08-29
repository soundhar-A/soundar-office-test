from django.urls import path
from .views import OfficeAPIView

urlpatterns = [
    path("",OfficeAPIView.as_view(),name="blog")
]
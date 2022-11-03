from lib2to3.pgen2.token import NAME
from django.urls import path
from .views import (HomeAPIView, DetailAPIView)

app_name = 'apis'

urlpatterns = [
    path('', HomeAPIView.as_view(), name='home'),
    path('detail/<slug:slug>', DetailAPIView.as_view(), name="detail"),
]

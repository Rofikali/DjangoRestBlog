
from unicodedata import name
from django.urls import path
# from .views import ( UserRegistrationView, UserLoginView)
from .views import (ListUsers, UserRegistrationView, UserLoginView)

app_name = 'accounts'

urlpatterns = [
    # path('users/<str:author>/', ListUsers.as_view(), name="usersonly"),
    path('user/register/', UserRegistrationView.as_view()),
    path('user/login/', UserLoginView.as_view()),
]


from unicodedata import name
from django.urls import path
# from .views import ( UserRegistrationView, UserLoginView)
from .views import (ListUsers,
                    UserRegistrationView,
                    UserLoginView,
                    UserProfileView
                    )

app_name = 'accounts'

urlpatterns = [
    path('users/', ListUsers.as_view()),
    path('user/register/', UserRegistrationView.as_view()),
    path('user/login/', UserLoginView.as_view()),
    path('user/profile/', UserProfileView.as_view()),
]

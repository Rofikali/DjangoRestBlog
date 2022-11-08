from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
from accounts.models import User

# simple jwt custom token
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (UserRegistrationSerializer,
                          UserLoginSerializer,
                          UserProfileSerializer
                          )


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.name for user in User.objects.all()]
        return Response(usernames)


class UserRegistrationView(APIView):
    '''
    User registration view with email, name, password, tc '''

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token': token, 'msg': 'Everything is ok here.'}, status=HTTP_201_CREATED)
        else:
            # print()
            # print()
            '''
            checking ErrorDetail keyboard inside Error fields or not
            '''
            # print(serializer.errors)
            # print()
            return Response({'msg': serializer.errors}, status=HTTP_400_BAD_REQUEST)

        ''' this is the main one here'''
        # def post(self, request, format=None):
        #     serializer = UserRegistrationSerializer(data=request.data)
        #     serializer.is_valid(raise_exception=True)
        #     user = serializer.save()
        #     token = get_tokens_for_user(user)
        #     return Response({'token': token, 'msg': 'Everything is ok here.'}, status=HTTP_200_OK)



class UserLoginView(APIView):
    '''
    User login view with email and password
    '''

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                # A backend authenticated the credentials
                token = get_tokens_for_user(user)
                return Response({'token': token, 'msg': 'Successfully logedin'}, status=HTTP_200_OK)
            else:
                return Response(
                    {'errors':
                     {'non_fileds_errors': [
                         'This email or password is not Valid']}
                     },
                    status=HTTP_200_OK
                )

        # No backend authenticated the credentials
        return Response({'errors': serializer.errors}, status=HTTP_400_BAD_REQUEST)

    ''' main one is this '''

    # def post(self, request, format=None):
    #     serializer = UserLoginSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     email = serializer.data.get('email')
    #     password = serializer.data.get('password')
    #     user = authenticate(emial=email, password=password)
    #     if user is not None:
    #         # A backend authenticated the credentials
    #         token = get_tokens_for_user(user)
    #         return Response({'token': token, 'msg': 'Successfully logedin'}, status=HTTP_200_OK)
    # else:
    #     return Response(
    #         {'errors':
    #          {'non_fileds_errors': [
    #              'This email or password is not Valid']}
    #          },
    #         status=HTTP_200_OK
    #     )


class UserProfileView(APIView):
    # login required
    # if request.user is same user

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response({'msg': serializer.data}, status=HTTP_200_OK)


class UserChangePasswordView(APIView):
    def get(self):
        return Response({'msg': 'Successfully logedin'}, status=HTTP_200_OK)


class SendPasswordResetEmailView(APIView):
    def get(self):
        return Response({'msg': 'Successfully logedin'}, status=HTTP_200_OK)


class UserPasswordResetView(APIView):
    def get(self):
        return Response({'msg': 'Successfully logedin'}, status=HTTP_200_OK)

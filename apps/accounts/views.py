from django.contrib.auth import  login
from rest_framework import generics, permissions, status
from rest_framework.settings import api_settings
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError

from knox.views import LoginView as KnoxLoginView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from .serializers import UserSerializer, AuthSerializer, RegisterUserSerializer
from .models import ShmisUser

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = ShmisUser.objects.order_by('-created').all()
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #authentication_classes = [SessionAuthentication, TokenAuthentication]

    @staticmethod
    @action(detail=False, url_path='profil', methods=['get'])
    def profil(request):
        if request.user.is_authenticated:
            return Response(
                UserSerializer(ShmisUser.objects.get(pk=request.user.id)).data,
                status=status.HTTP_200_OK
            )
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @action(detail=False, url_path='register', methods=['post'])
    def register(request):
        data = request.data
        if ShmisUser.objects.filter(email=data['email']):
            raise ValidationError('This email is already used. Please log in if it is your email address.')
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
class LoginView(KnoxLoginView):
    # login view extending KnoxLoginView
    serializer_class = AuthSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request,):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)    


"""
class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer



class ManageUserView(generics.RetrieveUpdateAPIView):

    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
    


class UserList(generics.ListCreateAPIView):
    queryset = ShmisUser.objects.all()
    serializer_class = UserSerializer
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
"""
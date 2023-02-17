from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.generics import RetrieveAPIView, CreateAPIView, GenericAPIView
from account.models import Custom_User
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from rest_framework import status



class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            return response

        except :
            context = {
            'status':status.HTTP_401_UNAUTHORIZED,
            'success': False,
            'message': 'Invalid Username or Password',
        }
            return Response(context,status=status.HTTP_401_UNAUTHORIZED)



class RegisterView(CreateAPIView):
    queryset = Custom_User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
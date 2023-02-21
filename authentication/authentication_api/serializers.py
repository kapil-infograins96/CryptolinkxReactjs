from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from account.models import Custom_User
import re,uuid,json
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer




reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
passObj = re.compile(reg)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_User
        fields = "__all__"

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # default_error_messages = {
    #     'no_active_account': 'email or password is incorrect!'
    # }
    username_field = Custom_User.EMAIL_FIELD

    def validate(self, attrs):
        email = attrs.get("email", None)
        password = attrs.get("password", None)
        data = dict()
        get_data = super(TokenObtainPairSerializer, self).validate(attrs)
        try:
            user = authenticate(email=email, password=password)
            refresh = self.get_token(user)
            data['status'] = status.HTTP_200_OK
            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)
            data['username'] = user.username.title()
            data['first_name']=user.first_name
            data['last_name']= user.last_name
            return data
        except (Custom_User.DoesNotExist, ValueError, TypeError, OverflowError):
            data["status"] = status.HTTP_401_UNAUTHORIZED
            data['response'] = "User is not exists.Please Register first!"
            return data
            
    @classmethod
    def get_token(cls, user):
        if user:
            token = super(MyTokenObtainPairSerializer, cls).get_token(user)
            token['username'] = user.username
            return token
        else:
            raise InvalidToken("User is not enabled.")

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Custom_User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    username = serializers.CharField(write_only=True, required=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = Custom_User
        fields = ('username','first_name','last_name','password','email','token')

    def validate(self, attrs):
        pass_regex1 = re.search(passObj, attrs['password'])
        if not pass_regex1:
            raise serializers.ValidationError({"password": "Password should include a capital later, a special character and numbers    !"})
        return attrs
        
    def create(self, validated_data):
        data = dict()
        get_uuid = uuid.uuid4()
        user = Custom_User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
       
     
        return user

    def get_token(self,instance):
        refresh = RefreshToken.for_user(instance)
        data = {}
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        self.token = data
        return self.token

    def to_representation(self,instance):
        try:
            data = super(RegisterSerializer,self).to_representation(instance)
            data['status'] = status.HTTP_201_CREATED
            data['success'] = True
            data['username'] = instance.username
            return data
        except Exception as exception:
            print(exception)
            

class Send_OTPSerializer(serializers.ModelSerializer):
    pass


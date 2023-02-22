from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.generics import RetrieveAPIView, CreateAPIView, GenericAPIView
from account.models import Custom_User
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer, Send_OTPSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.backends import TokenBackend
import random
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.conf import settings
from django.utils.html import strip_tags
from authentication.models import Email_OTP,KYC




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


class Send_OTP(APIView):
    def post(self, request,*args, **kwargs):
        try:
            token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
            valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
            get_logged_in_user = valid_data['user_id']
            get_user = Custom_User.objects.get(id=get_logged_in_user)
            mail = request.POST.get('email')

            if str(get_user) == str(mail):
                otp = random.randint(100000,999999)
                msg = f'your 6 digit OTP is {strip_tags(otp)}'
                subject = "Thanks for contacting Cryptolinkx"

                user = get_user
                email = mail
                otp = otp



                email_from = settings.EMAIL_HOST_USER
                
                send_mail(subject,msg,email_from, [mail],fail_silently=False)

                user = get_user
                email = mail
                otp = otp

                save_otp  = Email_OTP(user = user, email= email, otp = otp)
                save_otp.save()



                

                
                

            else:
                context = {
                'status':status.HTTP_401_UNAUTHORIZED,
                'success':False,
                'message':"This Email is not match with your login Email"
                }

                return Response(context, status=status.HTTP_401_UNAUTHORIZED)



           

            context = {
                'status':status.HTTP_201_CREATED,
                'success':True,
                'message':'OTP Sent on your Email'

            }
            return Response(context, status=status.HTTP_201_CREATED     )


        except Exception as E:
            context = {
                'status':status.HTTP_401_UNAUTHORIZED,
                'success':False,
                'message':str(E)

            }
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)


class Check_OTP(APIView):
    def post(self,request,*args, **kwargs):
        try:
            token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
            valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
            get_logged_in_user = valid_data['user_id']
            get_user = Custom_User.objects.get(id=get_logged_in_user)

            get_otp = Email_OTP.objects.get(user = get_user)
            user_otp = get_otp.otp
            print(type(user_otp))
            otp_post = request.POST.get('otp')
            post_otp =int(otp_post)
            print(type(post_otp))
            
            if user_otp == post_otp:
                get_user = Custom_User.objects.get(email = get_user)
                get_user.is_otp_verified = True
                get_user.save()
                get_otp.delete()

            else:
                context = {
                'status':status.HTTP_401_UNAUTHORIZED,
                'success':False,
                'message':"Invalid OTP"
                }

                return Response(context, status=status.HTTP_401_UNAUTHORIZED)


            context = {
                'status':status.HTTP_200_OK,
                'success':True,
                'message':'Email Verified'

            }
            return Response(context, status=status.HTTP_200_OK)


        except Exception as E:
            context = {
                'status':status.HTTP_401_UNAUTHORIZED,
                'success':False,
                'message':str(E)

            }
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)

class User_KYC_View(APIView):
    def post(self, request, *args, **kwargs):
        
        try:
            token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
            valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
            get_logged_in_user = valid_data['user_id']
            get_user = Custom_User.objects.get(id=get_logged_in_user)

            user = get_user.id
            document_type = request.POST.get('document_type')
            id_number = request.POST.get('id_number')
            kyc_front_pic = request.FILES.get('kyc_front_pic')
            kyc_back_pic = request.FILES.get('kyc_back_pic')
            kyc_selfie = request.FILES.get('kyc_selfie')
                                
            kyc_obj = KYC(user_id = user, document_type = document_type, id_number = id_number, doc_front_img = kyc_front_pic, doc_back_img = kyc_back_pic, doc_selfie = kyc_selfie)
            kyc_obj.save()

            context = {
                'status':status.HTTP_200_OK,
                'success':True,
                'message':'Documents Verification process is ongoing'

            }
            return Response(context, status=status.HTTP_200_OK)

        except Exception as E:
            context = {
                'status':status.HTTP_401_UNAUTHORIZED,
                'success':False,
                'message':str(E)

            }
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)

                
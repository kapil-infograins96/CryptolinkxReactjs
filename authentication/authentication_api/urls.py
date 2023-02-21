from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView,
    MyObtainTokenPairView,
    Send_OTP,
    Check_OTP
)

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('Otp_sent/',Send_OTP.as_view(), name = "sent-otp"),
    path('verify_otp/',Check_OTP.as_view(), name = "verify-otp")
   

]
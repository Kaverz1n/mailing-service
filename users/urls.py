from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import (
    UserRegisterView, UserLoginView, UserSentConfirmEmail, UserConfirmEmailView,
    UserConfirmedEmail, UserFailConfirmEmail, UserPasswordResetView, UserSentPassword
)

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sent_confirm_email/', UserSentConfirmEmail.as_view(), name='email_sent_confirm'),
    path('confirm_email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='email_confirm'),
    path('confirmed_email/', UserConfirmedEmail.as_view(), name='email_confirmed'),
    path('fail_confirm_email/', UserFailConfirmEmail.as_view(), name='email_fail_confirm'),
    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password_sent_email/', UserSentPassword.as_view(), name='password_sent_email')
]

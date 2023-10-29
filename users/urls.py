from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from users.apps import UsersConfig
from users.forms import CustomAuthenticationForm
from users.views import ProfileUpdateView, UserCreate, EmailVerify, ForgotPasswordView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login_form.html', form_class=CustomAuthenticationForm),
         name='user_login'),
    path('', LogoutView.as_view(), name='user_logout'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('create/', UserCreate.as_view(), name='user_create'),
    path('user_verify/', TemplateView.as_view(template_name='user_verify.html'), name='user_verify'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('forgot_password_success/', TemplateView.as_view(template_name='restore_password_success.html'),
         name='forgot_password_success'),
]

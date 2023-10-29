from django.contrib.auth.views import get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views.generic import UpdateView, CreateView, View
from django.views.generic.edit import FormView
from users.forms import CustomUserChangeForm, CustomCreationForm, ForgotPasswordForm
from users.models import User
from users.services import send_email_verify, generate_password


class ProfileUpdateView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserCreate(CreateView):
    model = User
    form_class = CustomCreationForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('users:user_verify')

    def form_valid(self, form):
        self.object = form.save()
        send_email_verify(self.request, self.object)
        self.object.is_active = False
        form.save()

        return super().form_valid(form)


class EmailVerify(View):
    User = get_user_model()

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        user.is_active = True
        user.save()
        return redirect('mail_sender:index')

    def get_user(self, uidb64):
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
        return user


class ForgotPasswordView(FormView):
    template_name = 'forgot_password.html'
    form_class = ForgotPasswordForm
    success_url = reverse_lazy('users:forgot_password_success')

    def form_valid(self, form):
        email = self.request.POST.get('email')
        user = User.objects.get(email=email)
        generate_password(user)
        return super().form_valid(form)


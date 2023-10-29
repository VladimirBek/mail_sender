from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.models import ModelForm
from django.forms import ValidationError
from users.models import User


class MixinFormStile:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CustomAuthenticationForm(AuthenticationForm, MixinFormStile):
    class Meta:
        model = User
        fields = ('email', 'password',)


class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class CustomUserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'avatar', 'phone_number', 'country')


class ForgotPasswordForm(ModelForm):

    def validate_unique(self):
        pass

    def clean_email(self):
        user_email = self.cleaned_data.get('email')
        if not User.objects.filter(email=user_email).exists():
            raise ValidationError('Пользователя с таким email не существует')
        return user_email

    class Meta:
        model = User
        fields = ('email',)

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from.models import UserProfile
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1','password2',)


class UserProfileForm(forms.ModelForm):
    phonenumber = PhoneNumberField(
        widget = PhoneNumberPrefixWidget(initial='IN')
    )

    class Meta:
        model = UserProfile
        fields =('phonenumber', 'city')
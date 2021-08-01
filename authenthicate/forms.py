from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, widgets
from.models import UserProfile, CafeProfile
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1','password2',)
    def __init__(self, *args, **kwargs ):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].help_text = '<span class="form-text text-muted"> <small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. </small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\’t be a commonly used password.</li><li>Your password can\’t be entirely numeric.</li> </ul>'


        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].help_text = '<span class="form-text text-muted"> <small>Enter the same password as before, for verification. </small></span>'


class CafeSignUpForm(UserCreationForm):
   

    class Meta:
        model = User
        fields = ('username',  'password1','password2',)

    def __init__(self, *args, **kwargs ):
        super(CafeSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].help_text = '<span class="form-text text-muted"> <small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. </small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\’t be a commonly used password.</li><li>Your password can\’t be entirely numeric.</li> </ul>'


        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].help_text = '<span class="form-text text-muted"> <small>Enter the same password as before, for verification. </small></span>'



class UserProfileForm(forms.ModelForm):
    phonenumber = PhoneNumberField( label="Select Country Code and Enter Your Phone Number ",
        widget =  PhoneNumberPrefixWidget(initial='IN')
    )
    city = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}) )

    class Meta:
        model = UserProfile
        fields =('phonenumber', 'city')

class CafeProfileForm(forms.ModelForm):
    cafeName = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = CafeProfile
        fields =('cafeName', 'image')
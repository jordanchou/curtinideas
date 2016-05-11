from django import forms
from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

#-----------------------------------------------------------------------------


class RegistrationForm(UserCreationForm):

    first_name = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)

    last_name = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)

    email = forms.EmailField(max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)

    sid = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)

    #password = CharField(widget=PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'sid', 'password1',
                  'password2')


#-----------------------------------------------------------------------------

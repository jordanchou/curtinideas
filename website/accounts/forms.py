from django import forms
from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

#-----------------------------------------------------------------------------


class RegistrationForm(UserCreationForm):

    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    email = forms.EmailField(label='Email')
    sid = forms.CharField(label='Student/Staff ID',
                          required=False, max_length=9)
    #password = CharField(widget=PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'sid', 'password1',
                  'password2')


#-----------------------------------------------------------------------------

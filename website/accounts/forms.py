from django import forms

class CreateUserForm(forms.Form):
	first_name = forms.CharField(label='First Name', max_length=30)
	last_name = forms.CharField(label='Last Name', max_length=30)
	email = forms.EmailField(label='Email')
	sid = forms.IntegerField(label='Student/Staff ID', required=False)
	password = CharField(widget=PasswordInput())
from django import forms
from .models import Submission
from django.contrib.admin import widgets as aw

class SubmissionForm(forms.ModelForm):
    title = forms.CharField( max_length=100,
                             widget=forms.TextInput(attrs={'class' : 'form-control'}),
                             required=False)

    text = forms.CharField( widget=forms.TextInput(attrs={'class' : 'form-control'}),
                            required=False)

    class Meta:
        model = Submission
        fields = ('title', 'text', 'category')

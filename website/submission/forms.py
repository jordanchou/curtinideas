from django import forms
from .models import Submission

class SubmissionForm(forms.ModelForm):
	title = forms

	class Meta:
		model = Submission
		fields = ('title', 'text')
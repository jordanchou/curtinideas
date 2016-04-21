from django import forms
from .models import Submission, Comment
from django.contrib.admin import widgets as aw

CATEGORIES = (
    ('Science and Engineering', 'Science and Engineering'),
    ('Health Sciences', 'Health Sciences'),
    ('Humanities', 'Humanities'),
)
#-----------------------------------------------------------------------------

class SubmissionForm(forms.ModelForm):
    title = forms.CharField( max_length=100,
                             widget=forms.TextInput(attrs={'class' : 'form-control'}),
                             required=False)

    text = forms.CharField( widget=forms.Textarea(attrs={'class' : 'form-control', 'cols':15, 'rows': 15}),
                            required=False)

    category = forms.ChoiceField(choices=CATEGORIES, required=True)
    class Meta:
        model = Submission
        fields = ('title', 'text', 'category')

#-----------------------------------------------------------------------------

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', 'is_improvement')

#-----------------------------------------------------------------------------

class CommentEditForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', 'is_improvement')

#-----------------------------------------------------------------------------
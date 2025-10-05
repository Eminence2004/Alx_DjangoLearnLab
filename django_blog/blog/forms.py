# blog/forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        data = self.cleaned_data['content']
        if len(data.strip()) < 3:
            raise forms.ValidationError("Comment is too short.")
        return data

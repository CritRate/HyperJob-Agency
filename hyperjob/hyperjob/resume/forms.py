from django import forms


class ResumeForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea, max_length=1024)

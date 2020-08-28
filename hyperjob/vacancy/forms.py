from django import forms


class VacancyForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea, max_length=1024)

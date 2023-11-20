from django import forms


class ReportForm(forms.Form):
    name = forms.CharField(max_length=30, min_length=2)
    email = forms.EmailField(max_length=70, min_length=4)
    project = forms.CharField(max_length=25)
    message = forms.CharField(widget=forms.Textarea, max_length=2000, required=False)
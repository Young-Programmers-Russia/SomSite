from django import forms
from .models import BugReport


class ReportForm(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = ['project', 'text']

from django import forms
from .models import Lead

class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)

class LeadModelForm(forms.ModelForm):
    # Meta to specify information about the form
    class Meta:
        model = Lead
        fields = (
            "first_name",
            "last_name",
            "age",
            "agent",
        )


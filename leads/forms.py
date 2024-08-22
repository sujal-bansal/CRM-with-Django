from django import forms
from .models import Lead

class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'
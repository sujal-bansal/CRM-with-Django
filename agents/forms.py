from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

User = get_user_model()

class AgentModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','username', 'first_name','last_name']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise ValidationError('This email is already in use. Please use a different email ')
        
        return email
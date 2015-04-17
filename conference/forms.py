from django import forms
from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email', ]
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control input-lg',
                                            'title': "Don't worry. We hate spam, and will not share your email with anyone.",
                                            'placeholder': "Enter your email address"})
        }
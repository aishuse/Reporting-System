from django import forms
from .models import MyUser


class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['email', 'date_of_birth', 'phone', 'role']
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "date_of_birth": forms.DateInput(),
            'phone': forms.NumberInput(attrs={"class": "form-control"}),
            'role': forms.Select(attrs={"class": "form-control"}),
        }


class LoginForm(forms.Form):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

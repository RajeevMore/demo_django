
from django.core import validators

from django import forms
from enroll.models import User

class StudentRegistrationForm(forms.ModelForm):  
    class Meta:
        model = User
        fields = ("name","email","password")
        labels = {'name': 'Enter Name', 'email' : "Enter Email ", 'password':'Enter Password'}
        widgets ={'password': forms.PasswordInput(render_value=True,)}

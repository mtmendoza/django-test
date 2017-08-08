#importing forms
from django import forms

class SignUpForm(forms.Form):
    name = forms.CharField(label='Enter your name' , max_length=100)
    email = forms.EmailField(label='Enter your email address' , max_length=100)

class PersonalDataForm(forms.Form):
    name = forms.CharField(label='Enter your name', max_length=100)
    email = forms.EmailField(label='Enter your email address' , max_length=100)
    phone = forms.CharField(label='Enter your phone number' , max_length=100)
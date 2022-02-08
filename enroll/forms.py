from calendar import c
from dataclasses import fields
from pyexpat import model
from django.core import validators
from django import forms
from .models import User

class MagasinRegistration(forms.ModelForm):
 class Meta:
     model= User
     fields = ['name', 'email', 'password']
     widgets ={
         'name': forms.TextInput(attrs={'class': 'form-control'}),
         'email': forms.EmailInput(attrs={'class': 'form-control'}),
         'password': forms.PasswordInput(attrs={'class': 'form-control'})

     }
from django import forms
from django.forms import ModelForm
from .models import ClientFeedback


#CREATE Feedback Form

class ClientFeedbackForm(ModelForm):
    email= forms.EmailInput()
    number= forms.TextInput() 
    name = forms.TextInput()
    message = forms.TextInput()
    class Meta: 
        model = ClientFeedback
        fields= ['email', 'number', 'name', 'message']

      


from django import forms
from django.contrib.auth.models import User
from .models import Business,Chat

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['business_image','business_name','business_email','business_service']
        
class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields=['message']
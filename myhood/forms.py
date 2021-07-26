from django import forms
from django.contrib.auth.models import User
from .models import Business,Chat,Profile

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['business_image','business_name','business_email','business_service']
        
class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields=['message']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['profile_pic','bio','phone_number']
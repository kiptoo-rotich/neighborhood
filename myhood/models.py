from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
import datetime as dt


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.CharField(blank=True,max_length=400)
    profile_pic = CloudinaryField('image',default='Image')
    phone_number=models.CharField(max_length=13)

    def __str__(self):
        return self.bio

class Neighborhood(models.Model):
    neighborhood_image = CloudinaryField('image',default='Image')
    neighborhood_name = models.CharField(max_length=50,null=True)
    neighborhood_location = models.CharField(max_length=30,null=True)
    admin = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.neighborhood_name
    
class TheUser(models.Model):
    name = models.CharField(max_length=15)
    neighborhood=models.ForeignKey('Neighborhood',null=True,on_delete=models.CASCADE)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.name
    
class Business(models.Model):
    business_image = CloudinaryField('image',default='Image')
    business_name = models.CharField(max_length=30)
    neighborhood = models.ForeignKey('Neighborhood',null=True,on_delete=models.CASCADE)
    business_name = models.EmailField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    business_service= HTMLField()
    business_email = models.EmailField(max_length=30)


    def __str__(self):
        return self.business_image
    
    @classmethod
    def search(cls,search_term):
        business=cls.objects.filter(business_name__icontains=search_term)
        return business
    
class Chat(models.Model):
    message = HTMLField()
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True, null=True)
    neighborhood=models.ForeignKey('Neighborhood',null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.user
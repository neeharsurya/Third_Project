from django.db import models

# Create your models here.
class Main_detials(models.Model):
    name = models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    
class Main_details_1(models.Model):
    name=models.CharField(max_length=100)
    vid = models.FileField(upload_to='videos/')
    
class Individual_parts_model(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
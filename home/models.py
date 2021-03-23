from django.db import models

# Create your models here.

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    email=models.CharField(max_length=50)
    content=models.TextField()
    timestamp=models.DateField(auto_now_add=True,blank=True)
    
    def __str__(self):
       return  'message from' + ' '+ self.fname
       

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class Posts(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.CharField(max_length=100)
    timestamp=models.DateField(blank=True)
    slug=models.CharField(max_length=130)
    thumbnail=models.ImageField( upload_to='images',blank=True)
    
    def __str__(self):
       return  self.title + ' by '+ self.author
   
class Usercomment(models.Model):
    sno=models.AutoField(primary_key=True)
    post=models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)
    
    
    def __str__(self):
        return self.comment[0:10] + "...."+"by"+ " "+self.user.username
       

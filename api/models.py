from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tytul = models.CharField(max_length=255)
    tresc = models.TextField()
    zdjecia = models.ImageField(upload_to='post_img',null=True,blank=True,default=None)
    data_utworzenia = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tytul

class Komentarz(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rodzic = models.ForeignKey("self", on_delete=models.CASCADE,null=True,blank=True,default=None)
    tresc = models.TextField(blank=False)
    data_utworzenia = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tresc

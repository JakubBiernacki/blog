from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageOps
import os
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tytul = models.CharField(max_length=255)
    tresc = models.TextField()
    zdjecia = models.ImageField(upload_to='post_img',null=True,blank=True,default=None)
    data_utworzenia = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tytul

    def save(self,*args, **kwargs):
        try:
            old_image = Post.objects.get(pk=self.pk).zdjecia
        except:
            old_image = False
        super().save(*args, **kwargs)

        if old_image:

            try:
                if old_image.url != self.zdjecia.url:
                    os.remove(old_image.path)
            except ValueError:
                os.remove(old_image.path)



class Komentarz(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rodzic = models.ForeignKey("self", on_delete=models.CASCADE,null=True,blank=True,default=None)
    tresc = models.TextField(blank=False)
    data_utworzenia = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tresc

    def save(self,*args, **kwargs):
        if self.rodzic:
            if self.rodzic.post == self.post:
                super(Komentarz,self).save(*args, **kwargs)
            else:
                return False
        else:
            super(Komentarz, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='profile_img/default.png',upload_to='profile_img',null=True,blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        try:
            old_image = Profile.objects.get(pk=self.pk).image
        except:
            old_image = False

        super().save(*args, **kwargs)
        if self.image:

            if self.image.url != '/media/profile_img/default.png' :

                img = Image.open(self.image.path)


                if (img.height >300 or img.width >300):

                    pil = ImageOps.exif_transpose(img)
                    w, h = pil.size

                    output_size = (300,300)

                    img.thumbnail(output_size)

                    if h>w:
                        img = img.rotate(270)
                        m_w, m_h = img.size
                        to_crop = (m_w - m_h) / 2

                        left = to_crop
                        top = 0
                        right = m_w - to_crop
                        bottom = m_h
                        img = img.crop((left, top, right, bottom))

                img.save(self.image.path)
        if old_image:

            if old_image.url != '/media/profile_img/default.png':
                os.remove(old_image.path)
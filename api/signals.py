from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
import os
from django.core.files.base import File
from django.contrib.auth.models import User
from .models import Profile,Post

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):

    instance.profile.save()

#usuwa plik po usunieciu profilu
@receiver(post_delete,sender=Profile)
def delete_profile_image(sender,instance,**kwargs):

    if instance.image.url != '/media/profile_img/default.png':
        try:
            os.remove(instance.image.path)
        except FileNotFoundError:
            pass
#ustawia domyślny obraz
@receiver(post_save,sender=Profile)
def set_default_image(sender,instance,**kwargs):

    if not instance.image:
        instance.image = 'profile_img/default.png'
        instance.save()


@receiver(post_delete,sender=Post)
def delete_post_image(sender,instance,**kwargs):

    if instance.zdjecia:
        try:
            os.remove(instance.zdjecia.path)
        except FileNotFoundError:
            pass
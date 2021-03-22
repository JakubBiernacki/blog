from django.contrib import admin
from .models import Post,Komentarz,Profile
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','user','tytul','data_utworzenia','zdjecia']
    search_fields = ['tytul']
    list_filter = ['user']

@admin.register(Komentarz)
class KomentarzAdmin(admin.ModelAdmin):
    list_display = ['id','user','post','tresc','data_utworzenia','rodzic_id']
    list_filter = ['post']

    search_fields = ['tresc']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','image']
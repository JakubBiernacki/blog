from rest_framework import serializers
from .models import Post,Komentarz

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class KomentarzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Komentarz
        fields = '__all__'
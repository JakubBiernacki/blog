from rest_framework import serializers
from .models import Post,Komentarz,Profile
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(read_only=True,default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'



class KomentarzSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Komentarz
        fields = '__all__'


    def validate(self,data):
        if data['rodzic']:
            if data['post']== data['rodzic'].post:
                return data
            raise serializers.ValidationError({'błędny rodzic': 'Nieprawidłowy rodzic'})
        return data



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('image',)


    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance



class UserSerializer(serializers.ModelSerializer):


    image = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username','email','first_name','last_name','image']


    def get_image(self, object):

        image = object.profile.image.url if object.profile.image else None

        return image



class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ['username','email','password','password2']
        extra_kwargs = {
            'password' : {'write_only':True,'style':{'input_type':'password'}}
        }

    def save(self, **kwargs):
        account = User(username=self.validated_data['username'],
                       email=self.validated_data['email']
                       )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Hasła w obu polach nie są identyczne'})

        account.set_password(password)
        account.save()
        return account


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}
        }
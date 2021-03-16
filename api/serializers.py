from rest_framework import serializers
from .models import Post,Komentarz,Profile
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class KomentarzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Komentarz
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image']
        # depth = 1


class UserSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(source='profile.image',required=False)

    class Meta:
        model = User
        fields = ['id', 'username','email','first_name','last_name','image']




    # def get_image(self, object):
    #     request = self.context.get('request')
    #     return request.build_absolute_uri(object.profile.image.url)

    # def save(self,instance, validated_data):
    #     instance.profile.image = self.validated_data.get('image',instance.image)
    #     super(UserSerializer, self).save(instance, validated_data)





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
from django.shortcuts import get_object_or_404
#API

from .models import Post,Komentarz
from django.contrib.auth.models import User
from django.contrib.auth import logout,login
from django.contrib.auth import authenticate
from .serializers import PostSerializer,KomentarzSerializer,UserSerializer,RegistrationSerializer,LoginSerializer,ProfileSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets,mixins

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    """
        API endpoint dla postów (od najnowszych)
        /<int:pk>/komentarze/ - wszystkie kometarze do posta (od najnowszych)
    """
    queryset = Post.objects.all().order_by("-data_utworzenia")
    serializer_class = PostSerializer

    @action(detail=True, methods=['get'])
    def komentarze(self,request,pk=None,*args,**kwars):

        post = Post.objects.get(pk=pk)
        queryset = post.komentarz_set.order_by('-data_utworzenia')

        serializer = KomentarzSerializer(queryset,many=True)

        return Response(serializer.data)

class KometarzeViewSet(viewsets.ModelViewSet):
    """
        API endpoint dla komentarzy
    """
    queryset = Komentarz.objects.all()
    serializer_class = KomentarzSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            rodzic = serializer.validated_data['rodzic']

            if rodzic:

                if rodzic.post == serializer.validated_data['post']:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({"Błąd":"Nieprawidłowy rodzic"}, status=status.HTTP_409_CONFLICT)


            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(  mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
            API endpoints
             user/<int:id> - szczegóły user
             user/<int:id>/profile - zmiana zdjecia profilowego
             user/<int:id>/posty - wszystkie posty użytkownika (od najnowszych)
             /login
             /logout
             /register
        """
    serializer_class = UserSerializer
    queryset = User.objects.all()


    def list(self,request):

        return Response( {"Wybierz jedną z opcji "},status=status.HTTP_200_OK)


    @action(detail=False, methods=['post'])
    def register(self, request):

        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'success':'konto zostało utworzone'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, methods=['get'])
    def logout(self,request):
        logout(request)
        return Response({'success':"zostałeś wylogowany"},status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def login(self,request):

        serializer = LoginSerializer(data=request.data)

        authenticated = authenticate(username=serializer.initial_data['username'],password=serializer.initial_data['password'])

        if authenticated:
            login(request,authenticated)
            return Response({'success': "zostałeś zalogowany"}, status=status.HTTP_200_OK)


        return Response({'error' : "złe dane"}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=True, methods=['get','put'])
    def profile(self,request,pk=None):
        profile = get_object_or_404(User.objects.select_related('profile'), pk=pk).profile
        if request.method == 'GET':

            serializer = ProfileSerializer(profile)

            return Response(serializer.data,status=status.HTTP_200_OK)

        else:
            serializer = ProfileSerializer(data=request.data)
            if serializer.is_valid():

                serializer.update(profile,serializer.validated_data)
                return Response({'success':'obrazek został zmieniony'}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def posty(self, request, pk=None):

        user = get_object_or_404(User.objects.prefetch_related('post_set'), pk=pk)


        serializer = PostSerializer(user.post_set.order_by('-data_utworzenia'),many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)


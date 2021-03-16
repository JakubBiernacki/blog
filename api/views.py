from django.shortcuts import render,get_object_or_404

#API
from rest_framework import viewsets,mixins

from .models import Post,Komentarz
from django.contrib.auth.models import User
from .serializers import PostSerializer,KomentarzSerializer,UserSerializer,RegistrationSerializer,LoginSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import logout,login

from django.contrib.auth import authenticate
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    """
        API endpoint dla wszystkich postów (od najnowszych)
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
        API endpoint dla wszystkich komentarzy
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


class UserViewSet(viewsets.ModelViewSet):
    """
            API endpoint dla user. user/<int:id> /login /logout /register
        """
    serializer_class = UserSerializer
    queryset = User.objects.all()


    def list(self,request):
        return Response( {"Podaj id usera lub wybierz opcje /login /logout /register"},status=status.HTTP_200_OK)

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = UserSerializer(instance,data=request.data,partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
        # instance = self.get_object()
        # print(request.FILES)
        # instance.profile.image = request.FILES.get('image')
        # instance.save()


    # def retrieve(self, request, pk=None):
    #
    #     user = get_object_or_404(User, pk=pk)
    #     serializer = UserSerializer(user,context={"request": request})
    #     return Response(serializer.data,status=status.HTTP_200_OK)



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










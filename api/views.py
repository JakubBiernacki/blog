from django.shortcuts import render,get_object_or_404

#API
from rest_framework import viewsets
from .models import Post,Komentarz
from .serializers import PostSerializer,KomentarzSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
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
            print(rodzic)
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



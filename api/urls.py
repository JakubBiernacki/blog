from django.urls import path,include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('posty',views.PostViewSet)
router.register('kometarze',views.KometarzeViewSet)
router.register('user',views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
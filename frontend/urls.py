from django.urls import path
from .views import index

urlpatterns = [
    path('',index),
    path('<str:user>/posts/',index),
    path('post/<str:id>/',index),

    path('post/<str:id>/edit/',index),
    path('post/<str:id>/delete/',index),

    path('login/',index),
    path('register/',index),
    path('profile/',index),
]
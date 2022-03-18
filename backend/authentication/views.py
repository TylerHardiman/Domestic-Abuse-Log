from django.contrib.auth import get_Survivor_model
from .views import MyTokenObtainPairSerializer, RegistrationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from survivor_main.models import Survivor


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = Survivor.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
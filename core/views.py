from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# Create your views here.

class LoginAPIView(APIView):
   def post(self,request):
      username = request.data.get('username')
      password = request.data.get('password')
      if username is None or password is None:
         raise ValidationError({
            "details":"Username and password are required."
         })
      
      user = authenticate(username = username, password = password)
      if user:
         token,_ = Token.objects.get_or_create(user = user)
         return Response(
            {
               "token":token.key,
               "username":username
               }
            )
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category
from .serializer import CategorySerializer
# Create your views here.
@api_view(['GET','POST'])
def category_list(request):
   if request.method =="GET":
      category = Category.objects.all()
      serializer = CategorySerializer(category,many=True)
      return Response(serializer.data)
   elif request.method == "POST":
      serializer = CategorySerializer(data = request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)
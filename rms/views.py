from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
from rest_framework import status
from rest_framework.validators import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
# from rest_framework import permissions
from .permission import IsAuthenticatedOrReadOnly
class CatergoryViewset(ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   
   def delete(self, request, pk):
      category = Category.objects.get(pk = pk)
      orderitem = OrderItem.objects.filter(food__category = category).count()
      if orderitem > 0:
         return Response({"details: This category exists in the order. Can not delete the category"})
      category.delete()
      return Response({"detail: Category deleted."}, status=status.HTTP_204_NO_CONTENT)

class FoodViewset(ModelViewSet):
   queryset = Food.objects.select_related('category').all()
   serializer_class = FoodSerializer
   pagination_class = PageNumberPagination
   permission_classes = [IsAuthenticatedOrReadOnly]

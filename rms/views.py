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
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.pagination import PageNumberPagination
# from rest_framework import permissions
from .permission import IsAuthenticatedOrReadOnly, IsWaiterOrReadOnly
from rest_framework import filters
from .filters import FoodFilter
from django_filters import rest_framework as filter
class CatergoryViewset(ReadOnlyModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   
   def delete(self, request, pk):
      category = Category.objects.get(pk = pk)
      orderitem = OrderItem.objects.filter(food__category = category).count()
      if orderitem > 0:
         return Response({"details: This category exists in the order. Can not delete the category"})
      category.delete()
      return Response({"detail: Category deleted."}, status=status.HTTP_204_NO_CONTENT)

class FoodViewset(ReadOnlyModelViewSet):
   queryset = Food.objects.select_related('category').all()
   serializer_class = FoodSerializer
   pagination_class = PageNumberPagination
   permission_classes = [IsAuthenticatedOrReadOnly]
   filter_backends = [filters.SearchFilter,filter.DjangoFilterBackend]
   filterset_class = FoodFilter
   # filterset_fields = ['name']
   search_fields = ['name', 'description']

class TableViewset(ReadOnlyModelViewSet):
   queryset = Table.objects.all()
   serializer_class = TableSerializer

class OrderViewset(ModelViewSet):
   queryset = Order.objects.prefetch_related('items').all()
   serializer_class = OrderSerializer
   pagination_class = PageNumberPagination
   permission_classes = [IsAuthenticatedOrReadOnly,IsWaiterOrReadOnly]

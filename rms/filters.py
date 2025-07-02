from django_filters import rest_framework as filters
from .models import Food

class FoodFilter(filters.FilterSet):
   class Meta:
      model = Food
      fields = {
         'category':['exact'],
         'price':['gt','lt']
      }
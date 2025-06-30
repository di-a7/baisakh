from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('category',CatergoryViewset)
router.register('food',FoodViewset)

urlpatterns = [
   # path("category/", CatergoryViewset.as_view({'get':'list','post':'create','delete':'destroy'})) # used to create path for viewsets
   # path('category/',category.as_view()),
   # path('category/<pk>/',category_detail.as_view()),
] + router.urls

from rest_framework import serializers
from .models import *
class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      fields = ["id","name"]
      # fields = '__all__'
      # exclude = ('id',)
   
   def save(self, **kwargs):
      validated_data = self.validated_data
      # Category.objects.all()
      total_number = self.Meta.model.objects.filter(name = validated_data.get('name')).count()
      if total_number > 0:
         raise serializers.ValidationError("Categroy already exists.")
      category = self.Meta.model(**validated_data)
      category.save()
      return category

class FoodSerializer(serializers.ModelSerializer):
   price_with_tax = serializers.SerializerMethodField()
   category = serializers.StringRelatedField()
   category_id = serializers.PrimaryKeyRelatedField(
      queryset = Category.objects.all(),
      source = 'category'
   )
   class Meta:
      model = Food
      fields =["id","name","description","price","price_with_tax","category_id","category"]
   
   def get_price_with_tax(self, food:Food):
      return food.price * 1.03 + food.price

class TableSerializer(serializers.ModelSerializer):
   class Meta:
      model = Table
      fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
   food_id = serializers.PrimaryKeyRelatedField(queryset = Food.objects.all())
   food = serializers.StringRelatedField()
   class Meta:
      model = OrderItem
      fields = ['food_id','food']

class OrderSerializer(serializers.ModelSerializer):
   User = serializers.HiddenField(default = serializers.CurrentUserDefault())
   items = OrderItemSerializer(many=True)
   status = serializers.CharField(read_only =True)
   payment_status = serializers.CharField(read_only =True)
   class Meta:
      model = Order
      fields = ['id','User','total_price','status','payment_status','items']
   
   def create(self, validated_data):
      items = validated_data.pop('items')
      order = Order.objects.create(**validated_data)
      
      for item in items: 
         OrderItem.objects.create(order = order, food = item['food_id'])
      
      return order
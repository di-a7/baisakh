from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Category(models.Model):
   name = models.CharField(max_length=15)

class Food(models.Model):
   name = models.CharField(max_length=20)
   description = models.TextField()
   price = models.FloatField()
   category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Table(models.Model):
   AVAILABLE = 'A'
   OCCUPIED = 'N'
   STATUS_CHOICE = {
      AVAILABLE:'Available',
      OCCUPIED:'Not Available',
   }
   number = models.CharField(max_length=2)
   status = models.CharField(max_length=1, choices = STATUS_CHOICE, default=AVAILABLE)

class Order(models.Model):
   PENDING = 'P'
   COMPLETED = 'C'
   PAID = 'P'
   UNPAID = 'U'
   STATUS_CHOICE = {
      PENDING:'Pending',
      COMPLETED:'Complete',
   }
   PAYMENT_STATUS = {
      PAID :'Paid',
      UNPAID :'Unpaid',
   }
   User = models.ForeignKey(User, on_delete=models.CASCADE)
   total_price = models.FloatField()
   status = models.CharField(max_length=1, choices=STATUS_CHOICE, default=PENDING)
   payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS, default=UNPAID)

class OrderItem(models.Model):
   order = models.ForeignKey(Order, on_delete=models.PROTECT)
   food = models.ForeignKey(Food, on_delete=models.PROTECT)
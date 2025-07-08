from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from django.core.mail import send_mail

@receiver(post_save, sender = Order)
def order_create(sender, instance, **kwargs):
   print("Order has been created.")
   
   send_mail(
      subject="Order",
      message="Order has been created.",
      from_email="rms@gmail.com",
      recipient_list=("a@gmail.com",)
   )


from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS
from rest_framework.serializers import ValidationError
class IsAuthenticatedOrReadOnly(BasePermission):
   def has_permission(self, request, view):
      return (request.method in SAFE_METHODS) or (request.user and request.user.is_authenticated)
      # return super().has_permission(request, view)

class IsWaiterOrReadOnly(BasePermission):
   def has_permission(self, request, view):
      if request.method in SAFE_METHODS:
         return super().has_permission(request, view)
      check_waiter = request.user.groups.filter(name = 'Waiter').exists()
      if not check_waiter:
         raise ValidationError({
            "details":"This user can not perform this action."
         })
      return check_waiter


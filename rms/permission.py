from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS
class IsAuthenticatedOrReadOnly(BasePermission):
   def has_permission(self, request, view):
      return (request.method in SAFE_METHODS) or (request.user and request.user.is_authenticated)
      # return super().has_permission(request, view)


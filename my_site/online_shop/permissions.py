from rest_framework import permissions
from rest_framework.permissions import BasePermission


class CheckStatus(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role =='owner'


class CheckOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner

class CheckOrder(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.order.client == request.user:
            return True
        return False

class UpdateCourier(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.order.courier == request.user

class CreateReview(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'client'

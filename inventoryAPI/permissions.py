from rest_framework import permissions


CREATE_METHOD = 'POST'

class IsStaffOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff or request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.method in permissions.SAFE_METHODS
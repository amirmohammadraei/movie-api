from rest_framework import permissions


class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.role == 2:
                return True
        except:
            return False


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.role == 1:
                return True
        except:
            return False


class AnonymousPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.id == None:
            return True
        return False
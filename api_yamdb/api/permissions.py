from rest_framework import permissions, status
from rest_framework.response import Response


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method not in permissions.SAFE_METHODS:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        return request.method in permissions.SAFE_METHODS


class AuthorAdminModeratorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_moderator()
            or request.user.is_admin()
            or request.user == obj.author
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    message = 'Для внесения изменений требуются права администратора'

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user.is_authenticated and request.user.is_admin())
        )


class AdminOnly(permissions.BasePermission):
    message = 'Требуются права администратора'

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin()

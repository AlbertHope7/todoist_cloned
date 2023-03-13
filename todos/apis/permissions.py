from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # authenticated users only can only see list view
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # allows read-only requests but limits write permissions to only the author of the task creator
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

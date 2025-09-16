from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Chỉ cho phép chủ sở hữu snippet được sửa hoặc xóa
    """
    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS thì ai cũng được
        if request.method in permissions.SAFE_METHODS:
            return True
        # Chỉ owner mới được PUT, DELETE
        return obj.owner == request.user

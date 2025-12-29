from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - Authenticated users: Can Read (GET).
    - Admin users: Can Create/Update/Delete (POST, PUT, PATCH, DELETE).
    """
    def has_permission(self, request, view):
        # 1. User must be logged in for any action
        if not request.user or not request.user.is_authenticated:
            return False

        # 2. Allow Read-only actions (GET, HEAD, OPTIONS) for any logged-in user
        if request.method in permissions.SAFE_METHODS:
            return True

        # 3. Only Admin users can write/edit (POST, PUT, DELETE)
        # We can use is_staff or check a specific group
        return request.user.is_staff or request.user.groups.filter(name='Admin').exists()
from rest_framework.permissions import BasePermission

# Generic base permission
class HasRole(BasePermission):
    def __init__(self, role):
        self.role = role

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == self.role


# Factory function to generate DRF-compatible permission classes dynamically
def RolePermission(role):
    class _RolePermission(HasRole):
        def __init__(self):
            super().__init__(role)
    return _RolePermission

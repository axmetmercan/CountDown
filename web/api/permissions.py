from rest_framework.permissions import BasePermission


# Will be added later on 
class IsBelongsTo(BasePermission):
    def has_object_permission(self, request, view, obj):
        isAuth = super().has_object_permission(request, view, obj)
        return True
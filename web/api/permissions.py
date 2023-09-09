from rest_framework.permissions import BasePermission



class ReadOnly(BasePermission):

    def has_permission(self, request, view):
        isAuth = super().has_permission(request, view)
        

        
        return True

class IsBelongsTo(BasePermission):
    def has_object_permission(self, request, view, obj):

        isAuth = super().has_object_permission(request, view, obj)


        
        return True
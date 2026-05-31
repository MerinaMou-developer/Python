from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    def has_objkect_permission(self,request,view,obj):
        if request.user.is_admin:
            return True
        return obj.user=request.user
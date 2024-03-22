from rest_framework.permissions import BasePermission


class IsCompanySuperAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        #return request.user.is_superuser
        return True
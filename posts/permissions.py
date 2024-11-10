from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission): # BasePermission has two types has or has_object. They will return boolean true or false. Only if has is true then has_object will work otherwise won't
    def has_permission(self, request, view): # has_permission gives entire model permission.That's why it's necessary to execute before has_object cause it a user can't get model permission then how will he get permission of a particular object permission
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
    
class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type=='admin'
    
class IsViewerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type=='viewer'
    
    
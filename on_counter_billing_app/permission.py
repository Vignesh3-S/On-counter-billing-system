from rest_framework import permissions

class Employee_Permission(permissions.BasePermission):
    message =  "You don't have the permission."
    
    def has_permission(self, request, view):
        if (request.user.is_authenticated) and (request.user.has_perm('on_counter_billing_app.add_employee')):
            return True
        return False

class Employee_Profile_Permission(permissions.BasePermission):
    message =  "You don't have the permission."
    
    def has_permission(self, request, view):
            if (request.user.is_authenticated):
                return True
    
    def has_object_permission(self, request, view, obj):
        if (request.user.is_authenticated) and (obj.Employee.Employee_username == request.user):
            return True
        
        return False

class Customer_Permission(permissions.BasePermission):
    message =  "You don't have the permission."
    
    def has_permission(self, request, view):
        if ((request.user.is_authenticated) and (request.user.Employee_department == 'Customer_Adder')) or (request.user.is_superuser == True):
            return True
    
    def has_object_permission(self, request, view, obj):
        if ((request.user.is_authenticated) and (request.user.Employee_department == 'Customer_Adder')) or (request.user.is_superuser == True):
            return True
        
        return False
    
class Product_Permission(permissions.BasePermission):
    message =  "You don't have the permission."
    
    def has_permission(self, request, view):
        if ((request.user.is_authenticated) and (request.user.Employee_department == 'Product_Adder')) or (request.user.is_superuser == True):
            return True
    
    def has_object_permission(self, request, view, obj):
        if ((request.user.is_authenticated) and (request.user.Employee_department == 'Product_Adder')) or (request.user.is_superuser == True):
            return True
        
        return False

class Product_Sell_Permission(permissions.BasePermission):
    message =  "You don't have the permission."
    
    def has_permission(self, request, view):
        if ((request.user.is_authenticated) and (request.user.Employee_department == 'Product_Seller')) or (request.user.is_superuser == True):
            return True
    
    def has_object_permission(self, request, view, obj):
        if ((request.user.is_authenticated) and (request.user.Employee_department == 'Product_Seller')) or (request.user.is_superuser == True):
            return True
        
        return False

    
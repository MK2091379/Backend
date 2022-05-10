from rest_framework.permissions import BasePermission 

class IsCompanyOwner(BasePermission):
    
    '''
    Allows access only CompanyOwner
        '''
    def has_permission(self, request, view):
       
         if request.user.role == 'C':
        
             return True
         
class IsEmployee(BasePermission):
    
    '''
    Allows access only CompanyOwner
        '''
    def has_permission(self, request, view):
       
         if request.user.role == 'E':
        
             return True
    
    
    
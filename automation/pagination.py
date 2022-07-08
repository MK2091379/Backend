from operator import imod
from rest_framework.pagination import PageNumberPagination 




class defult8_pagination(PageNumberPagination):
    PAGE_SIZE=8
    
class defult10_pagination(PageNumberPagination):
    PAGE_SIZE=10
    
class defult7_pagination(PageNumberPagination):
    PAGE_SIZE=7
    
class defult4_pagination(PageNumberPagination):
    PAGE_SIZE=4
    
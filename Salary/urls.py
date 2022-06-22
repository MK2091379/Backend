from django.urls import path
from . import views



urlpatterns = [
        path('addsalary/',views.AdminSalaryAPI.as_view({'post':'add_salary_for_employee'})),
        path('addsalary/update/<int:id>',views.AdminSalaryAPI.as_view({'patch':'add_salary_for_employee'})),
        path('showmysalary/',views.EomplyeeShowSalary.as_view({'get':'show_my_salary'})),

            
]
 
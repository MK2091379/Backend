from django import forms
from .models import Employee,CompanyOwner


class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = "__all__"
class CompanyOwnerForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = "__all__"

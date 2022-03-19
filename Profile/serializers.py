from dataclasses import field
from email.mime import image
from django.conf import settings
from rest_framework import serializers
from django.conf import settings
from Register.models import Company, User
from .models import Employee,CompanyOwner
#from Register import serializers

#class CompanySerializer(serializers.CompanySerializer.Meta):
#    pass
#class UserSerializer(serializers.ModelSerializer):
#    
#    role=serializers.CharField(read_only=True)
#    company=CompanySerializer(read_only=True)
#    class Meta:
#        model = User
#        fields=['first_name','last_name','phone','email','company','role','password']
class EmployeeSerializer(serializers.ModelSerializer):
#    user = UserSerializer()
#    class Meta:
#        model=Employee
#        fields=['user','birthdate','image','personal_id','father_full_name','mother_full_name','address','postal_code','sexuality','telephone','maritalـstatus','degreeـofـeducation']
#    def update(self, instance, validated_data):
#        user_data=validated_data.pop('user')
#        user=UserSerializer.update(UserSerializer(),validated_data=user_data)
#        Employee,created=Employee.objects.update(
#            user=instance,
#            birthdate=validated_data['birthdate'],
#            image=validated_data['image'],
#            personal_id=validated_data['personal_id'],
#            full_father_name=validated_data['father_full_name'],
#            full_mother_name=validated_data['mother_full_name'],
#            address = validated_data['address'],
#            postal_code = validated_data['postal_code'],
#            sexuality =validated_data['sexuality'],
#            telephone = validated_data['telephone'],
#            marital_status = validated_data['maritalـstatus'],
#            degree_of_education = validated_data['degreeـofـeducation']
#        )
#        user.save()
#        return user
    class Meta:
        model = Employee
        fields = "__all__"
class CompanyOwnerSerializer(serializers.ModelSerializer):
#    user = UserSerializer()
#    class Meta:
#        model=CompanyOwner
#        fields=['user','birthdate','image','personal_id','father_full_name','mother_full_name','address','postal_code','sexuality','telephone','maritalـstatus','degreeـofـeducation']
#    def update(self, instance, validated_data):
#        user_data=validated_data.pop('user')
#        user=UserSerializer.update(UserSerializer(),validated_data=user_data)
#        CompanyOwner,created=CompanyOwner.objects.update(
#            user=instance,
#            birthdate=validated_data['birthdate'],
#            image=validated_data['image'],
#            personal_id=validated_data['personal_id'],
#            full_father_name=validated_data['father_full_name'],
#            full_mother_name=validated_data['mother_full_name'],
#            address = validated_data['address'],
#            postal_code = validated_data['postal_code'],
#            sexuality =validated_data['sexuality'],
#            telephone = validated_data['telephone'],
#            marital_status = validated_data['maritalـstatus'],
#            degree_of_education = validated_data['degreeـofـeducation']
#        )
#        user.save()
#        return user
    class Meta:
        model = CompanyOwner
        fields = "__all__"
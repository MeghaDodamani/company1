from rest_framework import serializers
from .models import Employee,Department

class EmpSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
class DepSerilizer(serializers.ModelSerializer):
    employees = EmpSerilizer(many=True,read_only=True)
    class Meta:

        model = Department
        fields = '__all__' 
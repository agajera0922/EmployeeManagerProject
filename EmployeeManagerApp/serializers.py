from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    # Serializer to convert Employee objects to JSON
    manager_name = serializers.CharField(source='manager.emp_name', read_only=True)

    class Meta:
        # Specifying the model to use for the serializer
        model = Employee
        # Specifying the fields to include in the serialized representation
        fields = ('emp_id', 'emp_name', 'manager_name')

from rest_framework import generics

from .models import Employee
from .serializers import EmployeeSerializer


# Create a view that will return a list of employees
class EmployeeListView(generics.ListAPIView):
    # Define the queryset to be used to retrieve the employees from the database
    queryset = Employee.objects.all()
    # Define the serializer class to be used to serialize the employee data
    serializer_class = EmployeeSerializer

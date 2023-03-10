from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Employee
from .serializers import EmployeeSerializer


# Create a view that will return a list of employees
class EmployeeListView(generics.ListAPIView):
    # Define the queryset to be used to retrieve the employees from the database
    queryset = Employee.objects.all()
    # Define the serializer class to be used to serialize the employee data
    serializer_class = EmployeeSerializer

    def post(self, request):
        # Extract data from the request
        data = request.data

        # Create a serializer instance with the request data
        serializer = self.serializer_class(data=data)

        # If the serializer is valid, process the request data and create a new Employee object
        if serializer.is_valid():
            # Extract the manager_id from the request data
            manager_id = data.get('manager_id')

            # Ensure that the manager_id is not None
            if manager_id is None:
                return Response({'message': 'Manager ID cannot be None'}, status=status.HTTP_400_BAD_REQUEST)

            # Ensure that the manager_id is not the same as the employee ID
            if serializer.validated_data.get('emp_id') == manager_id:
                return Response({'message': 'Manager ID cannot be same as Employee ID'},
                                status=status.HTTP_400_BAD_REQUEST)

            # Ensure that the manager with the specified manager_id exists
            if serializer.validated_data.get('emp_id') != 1:
                manager = Employee.objects.filter(emp_id=manager_id).first()
                if manager is None:
                    return Response({'message': 'Manager not found'}, status=status.HTTP_404_NOT_FOUND)

            # Retrieve the manager object with the specified manager_id
            manager = Employee.objects.get(emp_id=manager_id)

            # Create a new Employee object with the validated request data and the specified manager object
            instance = serializer.save(manager=manager)

            # Serialize the new Employee object and return it in the response
            instance_serializer = self.serializer_class(instance)
            return Response(instance_serializer.data, status=status.HTTP_201_CREATED)

        # If the serializer is not valid, return an error response with the serializer errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailView(APIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'emp_id'

    def get(self, request, *args, **kwargs):
        # Get the emp_id parameter from the URL kwargs
        emp_id = self.kwargs.get('emp_id')

        # If emp_id is not None, retrieve the Employee object with that ID
        if emp_id is not None:
            # Filter the Employee queryset to retrieve the object with the specified emp_id
            queryset = Employee.objects.filter(emp_id=emp_id)

            # Set the name attribute of the queryset for use in the response
            queryset.name = "Employee Relationship"

            # If the queryset contains an Employee object, serialize it and return it in the response
            if queryset.exists():
                serializer = self.serializer_class(queryset.first())
                return Response(serializer.data)
            else:
                # If the queryset is empty, return a 404 error response
                return Response({'message': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            # If emp_id is None, retrieve all Employee objects and serialize them for the response
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

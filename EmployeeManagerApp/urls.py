from django.urls import path
from .views import EmployeeListView,EmployeeDetailView
# Defining urlpatterns as a list of URL patterns
urlpatterns = [
    # Creating a URL pattern for 'relationship/' endpoint, which maps to EmployeeListView view, with name 'employee_list - Handles POST and GET all'
    path('relationship/', EmployeeListView.as_view(), name='employee_list'),
    # Creating a URL pattern for 'relationship/emp_id' endpoint, which maps to EmployeeDetailView view, with name 'employee_detail - Handles GET by emp_id'
    path('relationship/<int:emp_id>/',EmployeeDetailView.as_view(), name = 'employee-detail'),
]

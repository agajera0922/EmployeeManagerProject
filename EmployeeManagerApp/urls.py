from django.urls import path
from .views import EmployeeListView

# Defining urlpatterns as a list of URL patterns
urlpatterns = [
    # Creating a URL pattern for 'relationship/' endpoint, which maps to EmployeeListView view, with name 'employee_list'
    path('relationship/', EmployeeListView.as_view(), name='employee_list'),
]

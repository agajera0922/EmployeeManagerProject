from django.apps import AppConfig

# AppConfig subclass for the EmployeeManagerApp app
class EmployeemanagerappConfig(AppConfig):
    # Set the default primary key field to use for models to BigAutoField
    default_auto_field = "django.db.models.BigAutoField"
    # Set the name of the app to 'EmployeeManagerApp'
    name = "EmployeeManagerApp"

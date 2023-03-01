from django.db import models

class Employee(models.Model):
    # Define the model fields
    emp_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    emp_name = models.CharField(max_length=255)  # Employee name with max length 255
    manager = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    # Manager field references the same model (self-referential), allows null and blank values, and will cascade delete

    def __str__(self):
        # Define the string representation of the object
        return f'{self.emp_name} ({self.emp_id})'

from django.test import TestCase
from .models import Employee

#define a test class for Employee model
class EmployeeModelTest(TestCase):
    def setUp(self):
        ceo = Employee.objects.create(emp_name='CEO')
        x = Employee.objects.create(emp_name='X', manager=ceo)
        w = Employee.objects.create(emp_name='W', manager=x)
        v = Employee.objects.create(emp_name='V', manager=w)
        u = Employee.objects.create(emp_name='U', manager=v)
        t = Employee.objects.create(emp_name='T', manager=u)
        s = Employee.objects.create(emp_name='S', manager=t)

        # assign the created objects to instance variables for later use in tests
        self.ceo = ceo
        self.x = x
        self.w = w
        self.v = v
        self.u = u
        self.t = t
        self.s = s

    # test the __str__ method of the Employee model
    def test_employee_str(self):
        self.assertEqual(str(self.ceo), 'CEO (1)')
        self.assertEqual(str(self.x), 'X (2)')
        self.assertEqual(str(self.w), 'W (3)')
        self.assertEqual(str(self.v), 'V (4)')
        self.assertEqual(str(self.u), 'U (5)')
        self.assertEqual(str(self.t), 'T (6)')
        self.assertEqual(str(self.s), 'S (7)')

    # test the manager attribute of the Employee model
    def test_employee_manager(self):
        self.assertEqual(self.x.manager, self.ceo)
        self.assertEqual(self.w.manager, self.x)
        self.assertEqual(self.v.manager, self.w)
        self.assertEqual(self.u.manager, self.v)
        self.assertEqual(self.t.manager, self.u)
        self.assertEqual(self.s.manager, self.t)

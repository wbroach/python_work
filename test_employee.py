import unittest
from employee import Employee

class TestEmployeeData(unittest.TestCase):
    
    def setUp(self):
        first = 'William'
        last = 'Broach'
        self.my_employee = Employee(first, last)
        
    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertTrue(self.my_employee.salary == 80000)
        
    def test_give_custom_raise(self):
        self.my_employee.give_raise(comp_inc=10000)
        self.assertTrue(self.my_employee.salary == 85000)
        
unittest.main()


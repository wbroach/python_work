class Employee():
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.salary = 75000
        
    def give_raise(self, comp_inc=5000):
        self.salary += comp_inc
        
    def show_salary(self):
        print(str(self.salary))



    # Class attribute to keep track of the total number of employees
class Employee:
    total_employees = 0

    def __init__(self, name, position, salary):
        self.name = name        
        self.position = position  
        self.salary = salary     
        Employee.total_employees += 1
    def display_info(self):
        return f"{self.name} works as a {self.position} with a salary of {self.salary}"
    @classmethod
    def get_total_employees(cls):
        return f"Total employees: {cls.total_employees}"
james = Employee("James", "cashier", 50000)
anna = Employee("Anna", "manager", 70000)
print(james.display_info()) 
print(anna.display_info())   
print(Employee.get_total_employees())  



class Employee:
    def __init__(self, name, position, salary):
        # Instance Attributes
        self.name = name        
        self.position = position  
        self.salary = salary    
    def display_info(self):
        return f"{self.name} works as a {self.position} with a salary of {self.salary}"

james = Employee("James", "cashier", 50000)

print(james.display_info())  

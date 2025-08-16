# 🧩 Problem 2: Employee Hierarchy
# Concepts: Constructors in parent/child, super()

# Create a class Employee that has:

# Attributes: name and salary

# A method display_info() that prints name and salary

# Then create a subclass Manager that:

# Has an extra attribute: department

# Overrides display_info() to also show the department

# Uses super() to reuse the parent constructor

# Goal: Practice constructor chaining and overriding methods.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name} \nSalary: {self.salary}")

class manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def display_info(self):
        print(f"\nName: {self.name} \nSalary: {self.salary} \nDepartment: {self.department}")

emp1 = Employee("Darshan", 20000)
emp1.display_info()

emp2 = manager("Prakash", 50000, "web dev")
emp2.display_info()
# Start Classes
'''
    from Employee import Employee
        --> create object from another file
'''

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    

emp = Employee("ahmed", 30, 200000)

print(emp)




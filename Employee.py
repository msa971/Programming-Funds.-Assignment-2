from Person import Person, Gender

class Employee(Person):
    """class to represent an employee"""

    #constructor:
    def __init__(self, name, id, age, gender, department, role):
        super().__init__(name, id, age, gender)
        self.department = department
        self.role = role

    #setter getter functions:
    def set_department(self, department):
        self.department = department

    def get_department(self):
        return self.department

    def set_role(self, role):
        self.role = role

    def get_role(self):
        return self.role
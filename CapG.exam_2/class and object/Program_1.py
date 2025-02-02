# Class and Object
# •	1. Create a class `Employee` with properties `name`, `id`, and `department`. Instantiate an object and assign values dynamically.
class Employee:
    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department


    def display(self):
        print("Name:", self.name)
        print("Id:", self.id)
        print("Department:", self.department)
obj=Employee("John", 101, "IT")
obj.display()


        
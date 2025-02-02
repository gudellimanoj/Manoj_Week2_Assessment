# •	7. Create a multi-level class structure with `Person` → `Employee` → `Manager`, where `Manager` has an additional method `approve_leave()`.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name: {self.name}\nAge: {self.age}"
class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id

    def display(self):
        return f"{super().display()}\nEmployee ID: {self.emp_id}"
class Manager(Employee):
    def __init__(self, name, age, emp_id, dept):
        super().__init__(name, age, emp_id)
        self.dept = dept

    def display(self):
        return f"{super().display()}\nDepartment: {self.dept}"

    def approve_leave(self):
        return "Leave Approved"
obj = Manager("John", 30, 101, "HR")
print(obj.display())
print(obj.approve_leave())
obj = Employee("Alice", 25, 102)
print(obj.display())
obj = Person("Bob", 22)
print(obj.display())

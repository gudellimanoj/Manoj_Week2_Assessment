# •	4. Implement a `Student` class with a constructor that initializes `name` and `roll_number`. Write a method to return student details.
class Student:
    def __init__(self, name, roll_no, department):
        self.name=name
        self.roll_no=roll_no
        self.department=department

    def display(self):
       return f"Name: {self.name}\nRoll No: {self.roll_no}\nDepartment: {self.department}"
obj=Student("John", 101, "IT")
print(obj.display())


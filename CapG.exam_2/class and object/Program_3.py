
# You are building a Library Management System. Create a `Book` class with properties like `title`, `author`, and `isbn`. Write a method to display book details.

class Book:
    def __init__(self, title, author, isbin):
        self.title=title
        self.author=author
        self.isbin=isbin
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Isbin:", self.isbin)
obj=Book("Python", "Guido van Rossum", 101)
obj.display()

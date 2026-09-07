students = {
    "John": 75,
    "Mary": 82,
    "Peter": 68,
    "Sarah": 90,
    "David": 77
}

print("Students and their marks:")

for name, mark in students.items():
    print(name, ":", mark)

highest_student = max(students, key=students.get)

print("Student with the highest mark:", highest_student)
print("Highest mark:", students[highest_student])


### 3(ii) Book Class

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


book1 = Book("Things Fall Apart", "Chinua Achebe", 15)
book2 = Book("The Alchemist", "Paulo Coelho", 20)

book1.display_details()

print()

book2.display_details()

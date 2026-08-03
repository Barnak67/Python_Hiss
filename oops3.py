class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
s1 = Student("Barnak", 100)
print(s1.name, s1.marks)
del s1.marks # delete the .marks attribute


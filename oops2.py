class Student:
    # if we dont have a constructor then 
    # python will create a default constructor
    def __init__(self):
        pass

    clg_name = "abc College" #class attribute

    #parameterized constructor
    def __init__(self, name, marks):
        self.name = name #obj attribute
        self.marks = marks
        print ("adding new databased into Databases")

    def welcome(self):
        print("hello students", self.name)

    def stuMark(self):
        print(self.marks)

s1 = Student("Barnak", 100)
s1.welcome()
s1.stuMark()

s2 = Student("Arjun", 60)
print(s2.name, s2.marks)

print(s2.clg_name)
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def avg(self):
        sum = 0 
        for i in self.marks:
            sum += i
        print("your avg marks is ", sum/3)
s1 = Student("Avi", [12, 21, 42]) 
print(s1.name, s1.marks)
s1.avg()
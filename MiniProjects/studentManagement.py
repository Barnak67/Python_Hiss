class Student:

    def __init__(self, name, roll, marks, stream):
        self.name = name
        self.roll = roll
        self.marks = marks
        self.stream = stream

    def __str__(self):
        return (f"Name: {self.name}\n"
               f"Roll: {self.roll}\n"
               f"Strean: {self.stream}\n"
               f"Marks: {self.marks}")
        
stud = []

def findStu(roll):
    for i in stud:
        if i.roll == roll:
            return i
    return None

def addStu():

    print("-----ADD STUDENT------")
    name = input("Enter Student name ")
    roll = int(input("Enter Student Roll: "))
    marks = int(input("Enter Student Marks: "))
    stream = input("Enter Student Stream: ")

    obj = Student(name, roll, marks, stream)
    stud.append(obj)
    print("Student added Successfully!")

def disStu():

    print("-----STUDENT LIST------")
    if len(stud) == 0:
        print ("NO STUDENT FOUND")
        return
    for i in stud :
        print(i)
        print("-" *30)

def searchStu():

    print("-----SEARCH STUDENT------")
    roll = int(input("Enter the Roll: "))
    std = findStu(roll)
    if std:
        print("Student Found")
        print(std) 
    else:
        print("Not Found")  

def updateStu():

    print("-----UPDATE STUDENT------")
    roll = int(input("Enter the Roll: "))
    for i in stud: 
        if i.roll == roll:
            print("CURRENT DETAILS")
            print(i)
            i.name = input("Enter Name: ")
            i.marks = int(input("Enter Student Marks: "))
            i.stream = input("Enter Student Stream: ")
            print("Student updated successfully")
            return
    print("Student Not Found")

def delStu():
    
    print("-----DELETE STUDENT------")
    roll = int(input("Enter the Roll: "))
    for i in stud:
        if i.roll == roll:
            stud.remove(i)
            print("Student removed Successfully")
            return
    print("Student Not Found")

while True:

    print("====STUDENT MANAGEMENT SYSTEM=====")
    print("1: Add Student")
    print("2: Display Student")
    print("3: Search Student")
    print("4: Update Student")
    print("5: Delete Student")
    print("6: Exit..")

    ch = int(input("Enter Your Choice: "))

    match ch:
        case 1: 
            addStu()
        case 2:
            disStu()
        case 3: 
            searchStu()
        case 4:
            updateStu()
        case 5:
            delStu()
        case 6:
            print("Thanks for visiting")
            break
        case _:
            print("Wrong Choice!")
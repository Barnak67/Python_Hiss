info = {
    "name" : "Barnak",
    "subjects" : ["python", "Java"],
    "topics" : ("Dictionaries",),
    "age" : 88,
    "is_adult" : True
}
info["age"] = 299
info["surname"] = "Banerjee"
print(info)
print(type(info))
print(info["age"])
print(info["topics"])
null_dict = {}
#nested dictionaries
student = {
    "name" : "Barnak",
    "subjects" : {
        "Maths" : 100,
        "Physics" : 100,
        "Chemistry" : 100
    }
}
print(student["subjects"])
print(student["subjects"]["Maths"])
#dictionary methods
print(student.keys())
print(len(list(student.keys())))
print(list(student.values()))
print(student.get("name"))#this is because it not gives error if wrong 
student.update({"city": "Ahmdabad"})
print(student)




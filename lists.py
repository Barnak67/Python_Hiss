#lists = array in java
lst1 = [ 10 , 20 , 30 , 40 , 80 , 100 ]
lst2 = ["Hello", "This", "is", "List"]
lst3 = ["Hello", 6.9, 67, True]

print ( lst1 ) # here the brackets will also be printed
print ( * lst1 ) # '*' is unpacking operator. 
#It takes all the elements out of a list (or tuple) and passes them one by one.

print(len(lst1)) #gives the length of the list
print(*lst2)
print(*lst3)
print(type(lst1))

print(lst1[-1]) # negetive indexing
print(*lst1[1:4]) # range [start:end] from start to end-1
print(*lst1[:4]) 
print(*lst1[2:])  




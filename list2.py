lst1 = [ 10 , 20 , 30 , 40 , 80 , 100 ]
#checking if item exists in the list
if 40 in lst1:
    print("Inside!")
#change value of a sp item
lst1 [4] = 50
print(lst1)
#Change a Range of Item Values
lst1 [4:6] = 9 , 0
print (lst1)
#insert item
lst1.insert(0, 0)
print (lst1)
#Append
lst1.append(10)
print(lst1)
#extend
lst2 = [30, 79, 12, 50]
lst1.extend(lst2)
print (lst1)
#remove
lst1.remove(0)
print (lst1) # remove the first occurance
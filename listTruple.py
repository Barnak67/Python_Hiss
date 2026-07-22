array = [1,2,3,4,5,6]
array.append(7)
array.insert(0,0)
print(array)
array.pop(3)
print(array)
#loop
for i in array:
    print(i, end = " ")
#for finding the index 
for i in range(len(array)):
    print( array[i])
#sorting list
lst1 = [4,2,65,2,1,6,7]
lst1.sort()#sort assending
print( lst1 ) 
lst1.sort(reverse=True)
print( lst1 )
#sort is case sensitive
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
thislist.sort(key = len, reverse = True)
print(thislist)

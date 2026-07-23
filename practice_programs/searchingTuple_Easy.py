lst = [2, 4, 4 ,23 , 3, 5, 6, 6, 6, 43 ,41234 ,234 ,2 ,23 ,424 , 78 ]
idx = 0
while (idx<len(lst)):
    print(lst[idx], end = " ")
    idx +=1
print()
tpl = (2, 4, 4 ,23 , 3, 5, 6, 6, 6, 43 ,41234 ,234 ,2 ,23 ,424 , 78 )
x = int(input("enter a number to be searched: "))
idx = 0
count = 0
while (idx<len(tpl)):
    if( x == tpl[idx]):
        count += 1
    idx +=1
if count == 0:
    print("Element not found")
else:
    print(x,"Found ", count, " times")
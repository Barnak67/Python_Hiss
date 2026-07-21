#while loop
i = 1
while i<=5:
    print( i , end = " " )
    i+=1
print()

#for loop
for i in range( 11 ): #range(stop)
    print( i , end = " " )
print()

for i in range( 0 , 11 ): #range(start, stop)
    print( i , end = " ")
print()

for i in range( 0 , 11, 2 ): #range(start, stop, step)
    print( i , end = " ")
print()

for i in range( 10 , 0 , -2 ): #range(start, stop, step)
    print( i , end = " ")
print()

for i in range( 0 , -11 , -2 ): #range(start, stop, step)
    print( i , end = " ")
print()
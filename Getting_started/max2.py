def find_maxMin (a, b):
    if (a>b):
        print ("The maximum number is : ", a)
    elif (b>a):
        print ("The maximum number is : ", b)
    else:
        print("The number are equal")
x = int(input("Enter a number : "))
y = int(input("Enter a number : "))
find_maxMin(x, y)
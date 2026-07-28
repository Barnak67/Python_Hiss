def findFibo(ed):
    a, b = 0, 1
    print (a, end= " ")
    print (b, end= " ")
    for i in range(2, ed, 1):
        c = a + b
        a = b
        b = c
        print(c, end= " ")

x = int(input("Enter a number: "))
findFibo(x)
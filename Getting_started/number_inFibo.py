#A number n is a Fibonacci number, 
# if and only if one or both of (5*n² + 4) or (5*n² – 4) is a perfect square
import math

def perfSq(num):
    s = int(math.sqrt(num))
    return s * s == num

def fibo(n):
    return perfSq(5 * n * n + 4 ) or perfSq( 5 * n * n - 4 )
num = int( input("Enter a number"))
for i in range (1, num+1):
    if (fibo(i)):
        print(i,"is a fibonacci number")
    else:
        print(i,"is not a fibonacci number")


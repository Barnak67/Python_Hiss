def countDigits(x):
    count = 0
    while x != 0:
        count += 1
        x //= 10
    return count


def checkarmNo(x):
    original = x
    totalDig = countDigits(x)
    total = 0

    while x != 0:
        rem = x % 10
        total += rem ** totalDig
        x //= 10

    return total == original


num = int(input("Enter a number: "))

if checkarmNo(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
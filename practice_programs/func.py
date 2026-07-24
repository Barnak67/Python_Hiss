cities = ["kolkata", "delhi", "mumbai", "nagpur"]
food = ["cookies", "tea", "chips", "fries"]
def pntLst(a):
    print(a)
def findLength(p):
    print (len(p))
findLength(cities)
findLength(food)
pntLst(cities)
pntLst(food)
n = int(input("Enter a number"))
def findFact(a):
    multi = 1
    i = 1
    while i <= n :
        multi *= i
        i +=1 
    print ("The factorial is is : ", multi)
findFact(n)
cost = float(input("Enter a number"))
def conUStoIR(c):
    newcost = c + 96.78
    return newcost
costUS = conUStoIR(cost)
print (costUS)
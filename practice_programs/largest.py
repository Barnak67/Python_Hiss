largeLst = list(map(int, input("Enter a list").split()))
max = float('-inf')
for i in largeLst:
    if max < i:
        max = i
print("the largest number is : " , max) 
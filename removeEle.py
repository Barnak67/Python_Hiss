a = [10, 20, 30, 40, 50, 60, 70]
remove = [20, 40, 60]
a = [x for x in a if x not in remove]
print(a)
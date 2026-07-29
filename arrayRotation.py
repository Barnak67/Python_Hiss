arr = [1, 2, 3, 4, 5, 6, 7, 8]
d = 2
n = len(arr)
arr.reverse()

arr[:n-d] = arr[:n-d][::-1]
arr[n-d:] = arr[n-d:][::-1]
print(arr)
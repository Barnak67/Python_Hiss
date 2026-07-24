def show(n):
    if ( n == 0 ):
        return 
    print(n)
    show(n-1)
show( 5 )
print()
def showAs(i, n):
    if i >= n:
        return

    print(i)
    showAs(i + 1, n)

showAs(1, 5)
    

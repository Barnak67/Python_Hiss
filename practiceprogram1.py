# to ask for 3 moveies
movielist = []
for i in range ( 3 ):
    movie = input("Enter your movie: ")
    movielist.append(movie)
print( movielist )
# to check palindrome
n = int(input("Enter the length of the list: "))
p1 = [] 
for i in range(n):
    p1.append(input("Enter: "))
p1Cpy = p1 . copy()
p1 . reverse()
if (p1Cpy == p1):
    print( " Palindrome" )
else:
    print( "Not Palindrome" )
# count tuple
tpl2 = ("C", "D", "E", "A", "F", "G", "C")
print(tpl2.count("A"))
tpl2.sort()
print(tpl2)


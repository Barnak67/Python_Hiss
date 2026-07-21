#if-else
print( " Enter your age" )
age = int(input())
if age >= 18:
    print( "You are eligible to vote" )
    if age == 18:
        print("have you applied for your voter card?")
        cho = str(input())
        if cho == "yes" or cho == "YES" or cho == "Yes":
            print("Soon you will be able to vote")
        else:
            print("apply now")
else:
    print( "you are not eligible to vote" )
#ternary operator
print( "number to check if it is a even" )
evenCheck = int(input())
check = bool( True if evenCheck %2 == 0 else False)
print(check)
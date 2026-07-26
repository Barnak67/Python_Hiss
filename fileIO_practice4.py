# from a file containing number seperated by commas print the count of even no.
with open ( "txt_demo5.txt" , "r") as f:
    data = f.read()
    print (data)
# first way of doing it 
    num = ""
    for i in range (len(data)):
        if (data[i] == ","):
            if (int(num) % 2 == 0):
                print (int(num))    
            num = ""
        else:
            num += data[i]

#better way of doing it
count = 0
with open ( "txt_demo5.txt" , "r") as f:
    data = f.read()
    num = data.split( "," )
    print(num)
    for vals in num:
        if(int(vals) % 2 == 0 ):
            print(int(vals))
            count += 1

print("Total no of even no are: ", count)
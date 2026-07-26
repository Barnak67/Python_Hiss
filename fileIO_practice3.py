#searching for a element in a file and counting the number of occurence
word = "-"
def searchThing (fileName):
    with open ( fileName, "r" ) as f:
        oldData = f.read()  
    if( oldData.find(word) != -1 ):
        print ( "FOUND!" )
        print ( oldData.count(word) )
    else:
        print ("Not Found")

#Now checking in which line the data exists 

def cek_for_line(filename):
    word = "practice1"
    data = True
    lineCount = 1
    with open ( filename, "r" ) as f:
        while data:
            data = f.readline()
            if ( word in data ):
                print(lineCount)
            lineCount += 1

searchThing( "txt_demo4.txt" )
cek_for_line( "txt_demo4.txt" )
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

searchThing( "txt_demo4.txt" )
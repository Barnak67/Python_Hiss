#replacing space by "-"
def spaceHy (fileName):
    with open ( fileName, "r" ) as f:
        oldData = f.read()  
    newData = oldData.replace( " ", "-")
    print(newData)
    with open ( fileName , "w" ) as f:
        f.write(newData)

spaceHy("txt_demo4.txt")





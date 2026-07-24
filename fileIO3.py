with open ( "txt_demo3.txt", "r" ) as f :
    data = f.read()
    print(data)
with open ( "txt_demo3.txt", "w" ) as f:
    f.write("OVER WRITTEN!")
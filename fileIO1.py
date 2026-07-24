file = open("txt_demo1.txt", "r")

data = file.read()
file.seek(0)
fst5char = file.read(5) #when we pass an argument here it reads that many chars
file.seek(0)
oneline = file.readline()

print(data)
print(fst5char)
print(type(data))
print(oneline)
file.close

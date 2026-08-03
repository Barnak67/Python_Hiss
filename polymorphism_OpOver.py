class Complex:
    def __init__(self, real, imgi):
        self.real = real
        self.imgi = imgi

    def showNum(self):
        print(str(self.real)+ "i +" +str(self.imgi)+ "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImgi = self.imgi + num2.imgi
        return Complex(newReal,newImgi)

    def __sub__(self, num2):
            newReal = self.real - num2.real
            newImgi = self.imgi - num2.imgi
            return Complex(newReal,newImgi)

num1 = Complex(1,2)
num2 = Complex(3,4)
num1.showNum()
num2.showNum()
num3 = num1 + num2
num3.showNum()
num4 = num1 - num2
num4.showNum()

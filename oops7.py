class Student:
    def __init__(self,phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.maths)/3) + "%"

st1 = Student(89,49,70)
print(st1.percentage)
class Person:
    name = "annonymous"
    
    # def changeName(self, name):
    #     self.__class__.name = "Arun"

    @staticmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName(p1, "Barnak")
print(p1.name)
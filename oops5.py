class Car:
    def __init__(self, egtype):
            self.egtype = egtype
    @staticmethod
    def start():
        print("Car has started...")

    @staticmethod
    def stop():
        print("Car has stopped....")

class Audi(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start()

car1 = Audi("someModelName","petrol")
print(car1.name,"\n", car1.egtype)
#multi level inheretance
class Car:

    @staticmethod
    def start():
        print("Car has started...")

    @staticmethod
    def stop():
        print("Car has stopped....")

class Audi(Car):
    def __init__(self, name):
        self.name = name

class SpModel(Audi):
    def __init__(self, egtype):
        self.egtype = egtype

car1 = SpModel("petrol")

print(car1.start())
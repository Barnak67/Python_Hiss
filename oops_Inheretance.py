#single level inheretance
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

car1 = Audi("someModelName")
car2 = Audi("someModelName")

print(car1.start())
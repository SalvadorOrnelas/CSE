class Vehicle(object):
    def __init__(self, seats, engine, turning_mechanism):
        self.seats = seats
        self.engine = engine
        self.turning_mechanism = turning_mechanism

    def move(self):
        print("you mave forward")

    def change_direction(self):
        print("you change direction")


class car(Vehicle):
    def __init__(self, seats, horsepower):
        super(car, self).__init__(seats, 'engine', 'steering wheel')
        self.hp = horsepower

    def turn_on(self):
        print("you turn the key and the engine starts")


test_car = car(4, 9001)
test_car.turn_on()
test_car.change_direction()
print(test_car.turning_mechanism)

class KeylessCar(car):
    def __init__(self, seats, hp):
        super(KeylessCar, self).__init__(seats, hp)

    def turn_on(self):
        print("you pushed the button and the car is turned on")


test_car.turn_on()
cool_car = KeylessCar(4, 9002)
cool_car.turn_on()



class Tesla(car):
    def __init__(self, seats):
        super(Tesla, self).__init__(seats, 500)

    def launch(self):
        print("you launch the car into low earth orbit")
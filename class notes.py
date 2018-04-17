# Defining a class
class Shoes(object):
    def __init__(self, lace_color, lighting, brand): # Two underscores before and after
        # Things a shoe has
        self.lace_color = lace_color
        self.rgb_lighting = lighting
        self.used = False
        self.brand = brand
        self.clean = True

    def wear(self):
        self.used = True
        self.clean = False
        print("You wear the shoes")

    def wash(self):
        self.wash = True
        print("You clean the shoe")


first_pair = Shoes("red", True, "balenciaga")
second_pair = Shoes("Black", False,"Gucci")

print(first_pair.brand)
print(second_pair.lace_color)
print(first_pair.clean)

first_pair.wear()
print(first_pair.clean)
first_pair.wash()
print(first_pair.clean)


class Car(object):
    def __init__(self, name, color, model, horsepower):
        self.name = name
        self.color = color
        self.model = model
        self.hp = horsepower
        self.running = False
        self.passengers = 0

    def drive_foward(self):
        if self.running:
            print("you move forward.")
        else:
            print("Nothing happens.")

    def turn_on(self):
        if self.running:
            print("nothing happened")
        else:
            print("You start the car")

    def turn_off(self):
        if self.running:
           self.running = False
           print("you turned off car")
        else:
          print("nothing happened")

    def go_for_drive(self, passengers):
        print("%d passengers get in" % passengers)
        self.passengers = passengers
        self.turn_on()
        self.drive_foward()
        self.drive_foward()
        self.drive_foward()
        self.turn_off()
        print("%d passengers get out" % passengers)
        self.passengers = 0


my_car = Car("Red", "Tesla", "x", 9001)
my_car.go_for_drive(4)

# Import Statements
# Class defintions
# Items
# Characters
# Rooms
# controller


class Item(object):
    def __init__(self, name, durability):
        self.name = name
        self.durability = durability


class Armor(Item):
    def __init__(self, name, durability):
        super(Armor, self).__init__(name, durability)
        self.durability -= 20


class Shield(Armor):
    def __init__(self):
        super(Shield, self).__init__("Shield", 80)

    def Block(self):
        print("You have a shield it will block anything from attacking")


class Helmet(Armor):
    def __init__(self):
        super(Helmet, self).__init__("Helmet", 65)

    def Wear(self):
        print("You have put on a helmet")


class Weapons(Item):
    def __init__(self, name):
        super(Weapons, self).__init__(name, 250)

    def Attack(self):
        print("you attacked")
        self.durability -= 10


class Sword(Weapons):
    def __init__(self):
        super(Sword, self).__init__("Sword")

    def Swung(self):
        print("You have swung the Sword")


class Assault_Rifle(Weapons):
    def __init__(self):
        super(Assault_Rifle, self).__init__("Assault rifle")

    def Shoot(self):
        print("You shot the gun")


class RPG(Weapons):
    def __init__(self):
        super(RPG, self).__init__("RPG")

    def Reload(self):
        print("You reloaded the RPG")


class Axe(Weapons):
    def __init__(self):
        super(Axe, self).__init__("Axe")

    def Throw(self):
        print("You have threw the Axe")


class Knife(Weapons):
    def __init__(self):
        super(Knife, self).__init__("Knife")

    def stab(self):
        print("You have been stabbed")


class Chancla(Weapons):
    def __init__(self):
        super(Chancla, self).__init__("chancla")

    def slapped(self):
        print("You have been slapped with a chancla")


class Clothing(Item):
    def __init__(self, name):
        super(Clothing, self).__init__(name)

    def Wear(self):
        print("You put on %s" % self.name)

    def Take(self):
        print("you took %s" % self.name)


class Raider_shirt(Clothing):
    def __init__(self):
        super(Raider_shirt, self).__init__("Raider shirt")

    def Put_on(self):
        print("You have put on the Raider shirt")


class Chicken_hat(Clothing):
    def __init__(self):
        super(Chicken_hat, self).__init__("Chicken hat")

    def Wear_hat(self):
        print("There is a chicken hat wear it")


class Belt(Clothing):
    def __init__(self):
        super(Belt, self).__init__("Belt")

    def Take_belt(self):
        print("There is a belt take it")


class Socks(Clothing):
    def __init__(self):
        super(Socks, self).__init__("Socks")

    def Slide_on(self):
        print("there some socks there how about you put them on")
        
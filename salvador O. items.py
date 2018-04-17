class Item(object):
    def __init__(self, name, durability):
        self.name = name
        self.durability = 200


class Armor(Item):
    def __init__(self, name):
        super(Armor, self).__init__(name)
        self.durability -= 20


class Shield(Armor):
    def __init__(self):
        super(Shield, self).__init__("Shield", 80)

    def Block(self):
        print("You have a shield it will block anything from attacking")


class Helment(Armor):
    def __init__(self):
        super(Helment, self).__init__("Helment", 65)

    def Wear(self):
        print("You have put on a helment")


class Shield_Postion(Armor):
    def __init__(self):
        super(Shield_Postion, self).__init__("Shield Postion", 50)

    def Drink(self):
        print("You have drunk the shield postion")


class Weapons(Item):
    def __init__(self, name, durability):
        super(Weapons, self).__init__(name)
        self.durability = 250

    def Attack(self):
        print("you attacked")
        self.durability -= 10


class Assault_Rifle(Weapons):
    def __init__(self):
        super(Assault_Rifle, self).__init__("Assault rifle", 45)

    def Shoot(self):
        print("You shot the gun")


class RPG(Weapons):
    def __init__(self):
        super(RPG, self).__init__("RPG", 100)

    def Reload(self):
        print("You reloaded the RPG")


class Axe(Weapons):
    def __init__(self):
        super(Axe, self).__init__("Axe", 45)

    def Throw(self):
        print("You have threw the Axe")


class Sword(Weapons):
    def __init__(self):
        super(Sword, self).__init__("Sword", 40)

    def Swung(self):
        print("You have swung the Sword")


class Belt(Weapons):
    def __init__(self):
        super(Belt, self).__init__("Belt", 25)

    def whip(self):
        print("You have been whipped by the belt")


class Knife(Weapons):
    def __init__(self):
        super(Knife, self).__init__("Knife", 20)

    def stab(self):
        print("You have been stabbed")


class Chancla(Weapons):
    def __init__(self):
        super(Chancla, self).__init__("chancla", 15)

    def slapped(self):
        print("You have been slapped with a chancla")


class Clothing(Item):
    def __init__(self, name):
        super(Clothing, self).__init__(name)

    def Wear(self):
        print("You put on %s" % self.name)


class Raider_shirt(Clothing):
    def __init__(self):
        super(Raider_shirt, self).__init__("Raider shirt")

    def Put_on(self):
        print("You have put on the Raider shirt")

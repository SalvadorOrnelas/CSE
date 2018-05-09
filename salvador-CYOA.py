# Import Statements
# Class Defintion
# Items
# Characters
# Rooms
# controller


class Item(object):
    def __init__(self, name):
        self.name = name


class Armor(Item):
    def __init__(self, name, durability):
        super(Armor, self).__init__(name)
        self.durability = durability


class Shield(Armor):
    def __init__(self):
        super(Shield, self).__init__("Shield", 80)


class Helmet(Armor):
    def __init__(self):
        super(Helmet, self).__init__("Helmet", 65)


class Weapons(Item):
    def __init__(self, name):
        super(Weapons, self).__init__(name)
        self.durability = 250

    def attack(self):
        print("you attacked")
        self.durability -= 10


class Sword(Weapons):
    def __init__(self):
        super(Sword, self).__init__("Sword")


class AssaultRifle(Weapons):
    def __init__(self):
        super(AssaultRifle, self).__init__("Assault rifle")


class RubberMallet(Weapons):
    def __init__(self):
        super(RubberMallet, self).__init__("rubber mallet")


class Knife(Weapons):
    def __init__(self):
        super(Knife, self).__init__("Knife")


class Sandle(Weapons):
    def __init__(self):
        super(Sandle, self).__init__("sandle")


class Clothing(Item):
    def __init__(self, name):
        super(Clothing, self).__init__(name)

    def wear(self):
        print("You put on %s" % self.name)

    def take(self):
        print("you took %s" % self.name)


class RaiderShirt(Clothing):
    def __init__(self):
        super(RaiderShirt, self).__init__("Raider shirt")


class ChickenHat(Clothing):
    def __init__(self):
        super(ChickenHat, self).__init__("Chicken hat")


class Belt(Clothing):
    def __init__(self):
        super(Belt, self).__init__("Belt")


class Socks(Clothing):
    def __init__(self):
        super(Socks, self).__init__("Socks")


class SoccerJersey(Clothing):
    def __init__(self):
        super(SoccerJersey, self).__init__("Soccer jersey")


class Shoes(Clothing):
    def __init__(self):
        super(Shoes, self).__init__("shoe")


class ChapionsHoodie(Clothing):
    def __init__(self):
        super(ChapionsHoodie, self).__init__("Chapions Hoodie")


class Accessorise(Item):
    def __init__(self, name):
        super(Accessorise, self).__init__(name)


class DiamondChain(Accessorise):
    def __init__(self):
        super(DiamondChain, self).__init__("diamond chain")


class Glasses(Accessorise):
    def __init__(self):
        super(Glasses, self).__init__("Glasses")


class Backpack(Accessorise):
    def __init__(self):
        super(Backpack, self).__init__("Backpack")


class Character(object):
    def __init__(self, name, inventory, description, health, location):
        self.name = name
        self.inventory = inventory  # List
        self.description = description
        self.health = health
        self.location = location

    def move(self, direction):
        self.location = globals()[getattr(self.location, direction)]

    def pick_up(self, item):
        self.inventory.append(item)
        print("You pick up the %s" % item.name)


char1 = Character("Salvador", [], "Short, long hair, etc", 100, "center of mall")

char2 = Character("Alberto", [], "tall, short hair, etc", 100, "center of mall")


class Room(object):
    def __init__(self, name, north, south, west, east, description, item=None):
        self.name = name
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.description = description
        self.item = item


# Initialize Items
hat = ChickenHat()
shirt = RaiderShirt()
socks = Socks()
belt = Belt()
sandle = Sandle()
shield = Shield()
mallet = RubberMallet()
sword = Sword()
knife = Knife()
gun = AssaultRifle()
helmet = Helmet()
shoes = Shoes()
hoodie = ChapionsHoodie()
chain = DiamondChain()
jersey = SoccerJersey()
glasses = Glasses()
bag = Backpack()

# Initialize Room
CENTEROFMALL = Room("Center of mall", 'OUTSIDEOFMALL', 'MENSMACYS', 'TILLYS', 'EXPRESS', "You are now in center"
                    " of the mall there are four ways to go which were are you going to go and will you buy")

OUTSIDEOFMALL = Room("Outside of mall", 'ALDOS', 'CENTEROFMALL', 'SHOEPALACE', "None", "You are now outside of"
                     "the mall there is four ways to go which way will you go")

SHOEPALACE = Room("Shoe palace", 'None', 'None', 'None', 'OUTSIDEOFMALL', "You are now in a shoe store there is shoes"
                  "for all ages there is only one way to get out from store", shoes)

ALDOS = Room("Aldos", 'None', 'OUTSIDEOFMALL', 'None', 'None', "You are in a store that sells dressing cloths there "
             "is only one way out and will you buys from store", belt)

BATHROOM = Room("Bathroom", 'None', 'None', 'OUTSIDEOFMALL', 'None', "Your in the bathroom there is only one way out"
                " are you going to go out are are you going to use the bathroom")

TILLYS = Room("Tillys", 'None', 'None', 'HOLLISTER', 'CENTEROFMALL', "You are now it tillys this store is for"
              " skaters there is two ways out will look around and buy", bag)

HOLLISTER = Room("Hollister", 'None', 'None', 'SHIEKH', 'TILLYS', "You are now in a name brand store where they sell "
                 "cloths for teens and adults there is two ways out", sandle)

SHIEKH = Room("Shiekh", 'None', 'None', 'RAIDERIMAGE', 'HOLLISTER', "You are now in another shoe store there is varity"
              " of shoes will u buy or leave there is only two way to get out", socks)

RAIDERIMAGE = Room("Raider image", 'None', 'PRESTIGO', 'None', 'None', "You are now in a store where they sell raider"
                   " gear and accessories will you look around or leave one way out", shirt)

PRESTIGO = Room("Prestigo", 'RAIDERIMAGE', 'None', 'None', 'None', "You are now int a room full with jewlrey will you"
                " buy or leave only one way out", chain)

MANSMACYS = Room("Mans Macys", 'CENTEROFMALL', 'INDOORSOCCER', 'ARCADE', 'None', "You are now in a store with only"
                 " boy and men clothing there is many types of clothing will buy or leave there is three ways out",
                 hoodie)

INDOORSOCCER = Room("Indoor Soccer", 'MENSMACYS', 'None', 'ARCADE', 'None', "You are is a indoor park where there is "
                    "two soccer fields will you play or leave two ways out", jersey)

ARCADE = Room("Arcade", 'None', 'None', 'None', 'INDOORSOCCER', " You are now in a arcade there is games all over there"
              " is only one way out will you play or leave", mallet)

EXPRESS = Room("Express", 'None', 'None', 'CENTEROFMALL', 'None', " You are now in a store where they sell casual"
               " clothing will you buy or leave", glasses)

LAZERTAG = Room("Lazer tag", 'EXPRESS', 'FUNJUMP', 'FOODCOURT', 'CENTEROFMALL', " You enter a room filled with lazers"
                " and guns will you play of leave there is one way out", gun)

FOODCOURT = Room("Food Court", 'LAZERTAG', 'FUNJUMP', 'CENTEROFMALL', 'None', " You are now at the food court there is"
                 " like 5 places to eat will eat there of will you go to another place to eat", knife)

FUNJUMP = Room("Fun Jump", 'None', 'FOODCOURT', 'LAZERTAG', 'CENTEROFMALL', " You are now at place where your kids can"
               " play and have fun will they stay and play of will they leave", helmet)

char1.location = CENTEROFMALL
directions = ["west", "east", "south", "north"]
short_directions = ["n", "e", "s", "w"]
while True:
    # Room info
    print(char1.location.name)
    print(char1.location.description)
    if char1.location.item is not None:
        print("There is a %s here" % char1.location.item.name)

    # Get input
    command = input('>_').lower().strip()

    # Pre-processing
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    # Process the command
    if command in directions:
        try:
            char1.move(command)
        except KeyError:
            print("you cannot go this way")
    elif 'take' in command:
        item_requested = command[5:]
        if char1.location.item is not None and item_requested.lower() == char1.location.item.name.lower():
            char1.inventory.append(char1.location.item)
            char1.location.item = None
            print("Taken")
    else:
        print("direction not recognized")

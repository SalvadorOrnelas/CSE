class Room(object):
    def __init__(self, name, north, south, west, east, description):
        self.name = name
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Room
CENTEROFMALL = Room("Center of mall", 'OUTSIDEOFMALL', 'MENSMACYS', 'TILLYS', 'EXPRESS', "You are now in center"
                      " of the mall there are four ways to go which were are you going to go and will you buy")
OUTSIDEOFMALL = Room("Outside of mall", 'ALDOS', 'CENTEROFMALL', 'SHOEPALACE', "None", "You are now outside of"
                       "the mall there is four ways to go which way will you go")
SHOEPALACE = Room("Shoe palace", 'None','None', 'None', 'OUTSIDEOFMALL', "You are now in a shoe store there is shoes"
                   "for all ages there is only one way to get out from store")
ALDOS = Room("Aldos", 'None', 'OUTSIDEOFMALL', 'None', 'None', "You are in a store that sells dressing cloths there "
             "is only one way out and will you buys from store")
BATHROOM = Room("Bathroom", 'None', 'None', 'OUTSIDEOFMALL', 'None', "Your in the bathroom there is only one way out"
                " are you going to go out are are you going to use the bathroom ")
TILLYS = Room("Tillys", 'None', 'None', 'HOLLISTER', 'CENTEROFMALL', "You are now it tillys this store is for"
              " skaters there is two ways out will look around and buy ")
HOLLISTER = Room("Hollister", 'None', 'None', 'SHIEKH','TILLYS', "You are now in a name brand store where they sell "
                 "cloths for teens and adults there is two ways out")
SHIEKH = Room("Shiekh", 'None', 'None', 'RAIDERIMAGE', 'HOLLISTER', "You are now in another shoe store there is varity"
              " of shoes will u buy or leave there is only two way to get out")
RAIDERIMAGE = Room("Raider image", 'None', 'PRESTIGO', 'None', 'None', "You are now in a store where they sell raider"
                    " gear and accessories will you look around or leave one way out")
PRESTIGO = Room("Prestigo", 'RAIDERIMAGE', 'None', 'None', 'None', "You are now int a room full with jewlrey will you"
                " buy or leave only one way out")
MANSMACYS = Room("Mans Macys", 'CENTEROFMALL', 'INDOORSOCCER', 'ARCADE', 'None', "You are now in a store with only"
                  " boy and men clothing there is many types of clothing for them and colone will buy or leave there is"
                  " three ways out")
INDOORSOCCER = Room("Indoor Soccer", 'MENSMACYS', 'None', 'ARCADE', 'None', "You are is a indoor park where there is "
                     "two soccer fields will you play or leave two ways out")
ARCADE = Room("Arcade", 'None', 'None', 'None', 'INDOORSOCCER', "You are now in a arcade there is games all over there"
              " is only one way out will you play or leave")
EXPRESS = Room("Express", 'None', 'None', 'CENTEROFMALL', 'None', "You are now in a store where they sell casual"
               " clothing will you buy or leave")
current_node = CENTEROFMALL
directions = ["west", "east", "south", "north", "northwest", "northeast", "southwest", "southeast"]
short_directions = ["n", "e", "s", "w", "ne", "nw", "se", "sw"]
while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("you cannot go this way")
    else:
        print("direction not recognized")
        print()
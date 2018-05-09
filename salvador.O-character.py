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

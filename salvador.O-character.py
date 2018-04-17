class Character(object):
    def __init__(self, name, inventory, description, health):
        self.name = name
        self.inventory = inventory
        self.description = description
        self.health = health

    def move(self):
        print("%s moves" % self.name)

    def talk(self):
        pass

char1 = Character("Salvador", [], "Short, long hair, etc", 100)
char1.move()

char2 = Character("Alberto", [], "tall, short hair, etc", 100)


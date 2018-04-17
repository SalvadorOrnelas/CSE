class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to cook" % self.name)


class Cooker(Person):
    def __init__(self, name, age, food):
        super(Cooker, self).__init__(name, age)
        self.skills = Cooker


class Chief(Cooker):
    def __init__(self, name, age, food, make_food):
        super(Chief, self).__init__(name, age, food)
        self.job = make_food

    def make_meal(self):
        print("you have made a top star meal for Chief Ramsay")
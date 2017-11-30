import random

print("hello world")

# Salvador Ornelas jr


print(3 + 5)
print(5 - 3)
print(3 * 5)
print(6 / 2)
print(3 ** 2)

print()  # this makes a new line. In python 3.6, it looks like: print()
print("see if you can figure this out")
print(5 % 3)

car_name = "salvador mobile"
car_type = "Magic school bus"
car_cylinders = 8
car_mpg = 9000.1

# Inline printing
print("I have a car called the %s" % car_name)

# # Asking for input
# name = input("whats your name? ") # in python 3, it is just called input()
# print("hello %s." % name)
#
# age = input("how old are you?") # in python 3, it is just called input()
# print("%s?! wow you are so young !" % age)
# song = input("whats your favorite song") # in python 3, is just called input
# print("%s?! wow that song is lit !" % song)

# functions


def print_hw():
    print("hello world")


print_hw()
print_hw()
print_hw()


def say_hi(name):
    print("hello %s." % name)
    print("enjoy your day.")


say_hi("timmy turner")


def print_age(name, age):
    print("%s is %d years old." % (name, age))
    age += 1  # age = age +1
    print("next year he will be %d" % age)


print_age("Timmy turner", 15)


def f(x):
    return x**3 + 4 * x**2 + 7 * x - 4


print(f(3))
print(f(4))
print(f(5))

# if statements

def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >=80 :
        return "B"
    elif percentage >= 70 :
        return "C"
    elif percentage >= 60 :
        return "D"
    elif percentage >= 50 :
        return "F"


'''write a function called "happy_bday"
that "sings" (prints) happy birthday


It must take one parameter called "name"
'''

def happy_bday(name):
    print("happy bithday to you")
    print("happy bithday to you")
    print("happy bithday dear " + name)
    print("happy bithday to you" + ".")

happy_bday("timmy")


# Loops

# for num in range (1000000):
#     print(num + 1)

# DO NOT RUN!!!
a = 1
while a < 10:
    print(a)
    a += 1


# random numbers

print (random.randint(0, 100))
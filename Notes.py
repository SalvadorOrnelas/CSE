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
 #name = input("whats your name? ") # in python 3, it is just called input()
 #print("hello %s." % name)
 #age = input("how old are you?") # in python 3, it is just called input()
 #print("%s?! wow you are so young !" % age)
 #song = input("whats your favorite song") # in python 3, is just called input
 #print("%s?! esketittttt !" % song)

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
#a = 1
#while a < 10:
    #print(a)
    #a += 1


# random numbers

#print (random.randint(0, 100))


# lists

#the_count = [1, 2, 3, 4, 5]
#shopping_list = ["Noodles", "eggrolls", "milk", "rice", "soda"]

#print(shopping_list[0])

#print(len(shopping_list))

# going through a list
#for item in shopping_list:
    #print(item)

#for num in the_count:
    #print(num * 2)

#len(shopping_list)  # Gives me the length of the list
#range(3)  # Gives a list of the numbers of 0 through 2
#range(len(shopping_list))  # A list of every index in a list

#for num in range(len(shopping_list)):
    #item = shopping_list[num]
    #print("the item at the index %d is %s" % (num, item))

# Turn things into a list
#str1 = "hello class!"
#listOne = list(str1)
#print(listOne)
#listOne[11] = '.'
#print(listOne)
#print("". join(listOne))

# Add things to a list
#shopping_list.append("Malic acid")
#print(shopping_list)

# Removing things from a list
#shopping_list.remove("soda")
#print(shopping_list)
#shopping_list.pop(0)
#print(shopping_list)

# The string class
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)
print(string.digits)

# Dealing with string
strTwo = "ThIs iS a VeRY oDd sEnTenCE"
lowercase = strTwo.lower()
print(lowercase)



dictionary = {'name': 'lance', 'age': 23, 'height': 5}


print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])

large_dictionary = {
    'CA': 'california',
    'FL': 'Florida',
    'OH': "Ohio"
}


print(large_dictionary['CA'])
print(large_dictionary['FL'])
print(large_dictionary['OH'])

larger_dictionary = {
    'CA': [
        "Fresno",
        "San Jose",
        "Los Angeles"
    ],
    'FL': [
        "Tampa",
        "Orlando",
        "Miami"
    ],
    'OH': [
        "Clevland",
        "cincinnati",
        "dayton"
    ]
}

print(larger_dictionary['OH'])
print(larger_dictionary["OH"][1])

largest_dictionary = {
    'CA': {
        'NAME': 'California',
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada',
            'Arizona'
        ]
    },
    'AZ': {
        'NAME': 'Arizona',
        'POPULATION': 6931000,
        'BORDER ST': [
            'California',
            'Utah',
            'Nevada',
            'New Mexico'
        ]
    },
    'NY': {
        'NAME': "New York",
        'POPULATION': 19750000,
        'BORDER ST': [
            'Vermont',
            'Massachusetts',
            'Connecticut',
            'Pennsylvania',
            'New Jersey'
        ]
    }
}
current_node = largest_dictionary['CA']
print(current_node)
print(current_node['NAME'])
print(current_node['POPULATION'])


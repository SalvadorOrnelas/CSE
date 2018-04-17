import random

money = 15
rounds = 0
max_money = money
max_rounds = 0

print("Welcome to lucky 7's")
print("These are the rules of the game")
print("You start off with 15 dollars")
print("Every time you play you bet 1$")
print("If you roll a 7 you get 4$ back and the dollar you betted")
print("If you don't get 7 you lose the dollar and keep playing till you lose")
print("good luck")

while money > 0:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    if dice1 + dice2 == 7:
        print("winner winner")
        money += 4

    else:
        print("tough luck")
        money -= 1
    print("money = %s" % money)
    rounds +=1
    if money == 0:
        print("you ran out of cash..... GAME OVERRR")

print("rounds = %s" % rounds)
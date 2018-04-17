import random

"""
A general guide for hangman
1. Make a word bank - 10 items
2. Pick an random item from the list
3. add a guess to the list of letters guess
4. Reveal letters already guessed
5. Create the win condition
"""
guesses_left = 10

    if output == list(random_word):
        print("Congrats You Win

word_bank = ["soccer", "edison", "tigers", "lamborghini", "basketball", "esketit", "gucci", "football", "faze", "f2"]
random_word = word_bank[random.randint(0, len(word_bank) - 1)]
# print(random_word)
letters_guessed = []

current_guess = ''
win = False
while guesses_left > 0 and not win:
    output = []
    for letter in random_word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(" ".join(list(output)))")
        win = True
        continue
    current_guess = input("Type in a letter: ")
    letters_guessed.append(current_guess)
    print(letters_guessed)

    if current_guess not in random_word:
        guesses_left -= 1
        print(guesses_left)

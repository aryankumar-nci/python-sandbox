#Step 2

import random
word_list = ["baboon", "camel","elephant"]
chosen_word = random.choice(word_list)

#Testing code

print(chosen_word)

placeholder=""
for char in chosen_word:
    print("_",end='')
print("\n")

game_over =False

while not game_over:
    guess = input("Guess a letter: ").lower()
    display =""

    for letter in chosen_word:
        if letter == guess:
            display+=letter
        else:
            display+="_"
    print(display)

 
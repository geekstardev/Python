import random
from hangman_words import word_list

choosen_word = random.choice(word_list)

flag = False
lives = 6

from hangman_art import logo
print(logo)

display = []
for _ in range(len(choosen_word)):
    display += "_"

while not flag:

    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guesssed {guess}")

    for i in range(len(choosen_word)):
        letter = choosen_word[i]
       # print(f"Current position: {i} \n Current letter: {letter}\n Guesses letter: {guess} ")
        if letter == guess:
            display[i] = letter
    
    if guess not in choosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
    if lives == 0:
        flag == True
        print("You Lose")

    print(f"{' '.join(display)}")

    if "_" not in display: 
        flag = True
        print("You win!!")
    
    from hangman_art import stages
    print(stages[lives])
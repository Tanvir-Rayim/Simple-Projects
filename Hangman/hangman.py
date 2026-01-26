import random
from hangman_words import word_list
from hangman_art import stages, logo

print(f"Welcome to Hangman!\n{logo}")
rand_word = random.choice(word_list)
display = []
for _ in rand_word:
    display.append("_")

game_status = "win"
lives = 6
guessed_letters = []

while lives>0 and "_" in display:
    print(f"{'*' * 10}{lives}/6 LIVES LEFT{'*' * 10}")
    guess = input("Enter any letter: ").lower()
    if guess in guessed_letters:
        print("Can not enter same letter twice")
    else:
        guessed_letters.append(guess)
    for i, val in enumerate(rand_word):
        if guess == val:
            display[i] = guess
    print(''.join(display))
    if guess not in rand_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            game_status = "lose"

if game_status == "win":
    print("You win!")
else:
    print(f"You lose! The word was {rand_word}.")
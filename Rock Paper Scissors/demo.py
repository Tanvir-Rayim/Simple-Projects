import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Simplified version using a 2D lookup table
values = [rock, paper, scissors]
choices = ["Rock", "Paper", "Scissors"]

user = int(input("What do you choose? 0: Rock, 1: Paper, 2: Scissors: "))

if 0 <= user < 3:
    computer = random.randint(0, 2)
    
    print(f"You picked {choices[user]}")
    print(values[user])
    print(f"Computer picked {choices[computer]}")
    print(values[computer])
    
    # Win conditions: 0 beats 2, 1 beats 0, 2 beats 1
    # Or simplified: (user - computer) % 3
    if user == computer:
        print("Draw!")
    elif (user - computer) % 3 == 1:
        print("You Win!")
    else:
        print("You Lose!")
else:
    print("Enter a valid number!")

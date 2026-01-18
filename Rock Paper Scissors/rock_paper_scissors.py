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

values = [rock, paper, scissors]
user = int(input("What do you choose? 0: Rock, 1: Paper, 2: Scissors: "))
pick = random.choice(values)
if 0 <= user < 3:
    user_pick = values[user]
    print("You picked ", user_pick)
    print("computer picked ", pick)
    if user_pick == rock:
        if pick == paper:
            print("You Loose!")
        elif pick == scissors:
            print("You Win!")
        else:
            print("Draw!")
    elif user_pick == paper:
        if pick == scissors:
            print("You Loose!")
        elif pick == rock:
            print("You Win!")
        else:
            print("Draw!")
    else:
        if pick == rock:
            print("You Loose!")
        elif pick == paper:
            print("You Win!")
        else:
            print("Draw!")
else:
    print("Enter a valid number!")
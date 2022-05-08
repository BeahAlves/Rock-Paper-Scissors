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

import random

#USER
print("Welcome to the Rock, Paper and Scissors game! :D ")
user_choice = input("Please, type 1 for Rock; 2 for Paper or 3 for Scissors. ")
if user_choice == '1':
    print(f'You chose: {rock}')
elif user_choice == '2':
    print(f'You chose: {paper}')
elif user_choice == '3':
    print(f'You chose: {scissors}')

#COMPUTER
pc_choice = random.randint(1,3)
print(f"The computer choice was: ")
if pc_choice == 1:
    print(rock)
elif pc_choice ==2:
    print(paper)
elif pc_choice == 3:
    print(scissors)

#CHOICES
if pc_choice == 1 and user_choice == '1':
    print("Draw")
elif pc_choice == 1 and user_choice == '2':
    print(("You won! :D "))
elif pc_choice == 1 and user_choice == '3':
    print("You lost. :( ")
elif pc_choice == 2 and user_choice == '1':
    print("You lost. :( ")
elif pc_choice == 2 and user_choice == '2':
    print("Draw")
elif pc_choice == 2 and user_choice == '3':
    print(("You won! :D "))
elif pc_choice == 3 and user_choice == '1':
    print(("You won! :D "))
elif pc_choice == 3 and user_choice == '2':
    print("You lost. :( ")
elif pc_choice == 3 and user_choice == '3':
    print("Draw")
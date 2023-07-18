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
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors. \n"))
computer_choice = random.randint(0, 2)
#print(computer_choice)

#Player Win Conditions
if player_choice == 0 and computer_choice == 2:
  print(rock)
  print("Computer chose:\n")
  print(scissors)
  print("You win!")
elif player_choice == 1 and computer_choice == 0:
  print(paper)
  print("Computer chose:\n")
  print(rock)
  print("You win!")
elif player_choice == 2 and computer_choice == 1:
  print(scissors)
  print("Computer chose:\n")
  print(paper)
  print("You win!")

#Player Lose Conditions
if player_choice == 0 and computer_choice == 1:
  print(rock)
  print("Computer chose:\n")
  print(paper)
  print("You lose.")
if player_choice == 1 and computer_choice == 2:
  print(paper)
  print("Computer chose:\n")
  print(scissors)
  print("You lose.")
if player_choice == 2 and computer_choice == 0:
  print(scissors)
  print("Computer chose:\n")
  print(rock)
  print("You lose.")

#Tie Conditions
if player_choice == computer_choice:
  if player_choice == 0:
    print(rock)
  elif player_choice == 1:
    print(paper)
  elif player_choice == 2:
    print(scissors)

  print("Computer chose:\n")
  if computer_choice == 0:
    print(rock)
  elif computer_choice == 1:
    print(paper)
  elif computer_choice == 2:
    print(scissors)
    
  print("You tied.")
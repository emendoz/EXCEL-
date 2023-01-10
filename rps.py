""" Rock, Paper, Scissor Program """

import random

print("This is the Rock, Paper, Scissor Program!")
player_choice = input("Rock, Paper, or Scissor? ")
player_choice = player_choice.capitalize()

# Generate a number between 1 and 3
number = random.randint(1,3)

# Assign the value, "Rock", "Paper", or "Scissor" to computer_choice
# depending on whether the number generated is 1,2, or 3
if number == 1:
    computer_choice = "Rock"
elif number == 2:
    computer_choice = "Paper"
else:
    computer_choice = "Scissor"

# Compare the player's choice to the computer's choice to determine who wins
if player_choice == computer_choice:
    print("Tie!")
elif ((player_choice == "Rock" and computer_choice == "Paper") or 
     (player_choice == "Paper" and computer_choice == "Scissor") or
     (player_choice == "Scissor" and computer_choice == "Rock")):
    print("You lose! ", computer_choice, " beats ", player_choice)
elif (player_choice != "Rock") or (player_choice != "Paper") or (player_choice != "Scissor"):
    print("That's not a valid play. Check your spelling!")
else:
    print("You win! ", player_choice, " beats ", computer_choice)
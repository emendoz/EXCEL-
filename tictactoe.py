""" Tictactoe game for 2 players """

# Assign the array that will hold the tic-tac-toe values to null
choices = []

# Fill in the squares with numbers 1 to 10
for x in range (0,9):
    choices.append(str(x + 1))

playerOneTurn = True
winner = False

# Display the Tic-tac-toe board
def printBoard():
    print('\n-------')
    print('|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print('-------')
    print('|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print('-------')
    print('|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print('-------\n')
    
# Keep playing while there is still no winner
while not winner:
    printBoard()

    if playerOneTurn:
        print("Player 1:")
    else:
        print("Player 2:")

    # Allow the user to select a square
    choice = int(input(">> "))

    # If the user enters a value outside of the range 1-10
    # display andf error message and prompt the user to reenter again
    while (choice < 1) or (choice > 9):
        print("Please enter a value between 1 and 10.\n")
        choice = int(input(">> "))
    
    # If the user selects a square that already has an "X" or "O", 
    # display an error message and prompt the user to reenter again
    if choices[choice - 1] == 'X' or choices[choice - 1] == 'O':
        print("Illegal move, please try again.")
        continue

    # Put an "X" or an "O" in the square that the user selected 
    if playerOneTurn:
        choices[choice - 1] = 'X'
    else:
        choices[choice - 1] = 'O'

    # Check each row and column starting from column 1, row 1 to column 3
    # row 3 to see if there are three X's or three O's.
    for x in range (0,3):
        y = x * 3
        # print(x, "", y)
        if(choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]):
            winner = True
            printBoard()
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]):
            winner = True
            printBoard()

        
    # Check each of the two diagonals to see if there are three X's or three O's
    if((choices[0] == choices[4] and choices[0] == choices[8]) or
      (choices[2] == choices[4] and choices[4] == choices[6])):
        winner = True
        printBoard()

    # Assign next plater's turn
    playerOneTurn = not playerOneTurn

print("Player " + str(int(playerOneTurn + 1)) + " wins!\n")
    
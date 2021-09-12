# Imports
import re
import random

# Input from user
print('''
This is a rock-paper-scissors game.
Input the following:
''')

playerWins = 0
computerWins = 0

def playerInput():
    while True:
        global player
        player = input("'r' for rocks, 'p' for paper, 's' for scissors:\n").lower()
        gamePattern = re.search(r"[rpsq]", player)
        if gamePattern and len(player) == 1:
            break
        elif not gamePattern and (len(player) > 2) or (len(player) < 1):
            print("Please type 'r' for rock, 'p' for paper, and 's' for scissors")

def play():
    playerInput()
    computer = random.choice(['r', 'p', 's', 'p', 'r', 's'])
    if not player == "q":
        print("Computer: {}".format(computer))
    global playerWins
    global computerWins
    
    if player == computer:
        print("It is a tie.")
        computerWins += 0
        playerWins += 0
    elif (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
        print("You've won! :)")
        playerWins += 1
    elif (player == 'q'):
        exit()
    else:
        print("You've lost! :(")
        computerWins +=1
    print("Player: {}\nComputer: {}".format(playerWins, computerWins))

def nthPlay(userWins, opponentWins):
    while True:
        if userWins >= opponentWins + 2:
            print("Match Over! You've won! :)")
            break
        elif opponentWins >= userWins + 2:
            print("Match Over! You've lost! :(")
            break
        play()

nthPlay(playerWins, computerWins)
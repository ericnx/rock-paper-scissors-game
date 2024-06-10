import random
from enum import IntEnum

class Pick(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3

# Get the player's pick
def get_player_pick():
    while True:
        try:
            player_pick = input("Enter a number: 1 for Rock, 2 for Paper, or 3 for Scissors\n")
            pick = Pick(int(player_pick))
            break
        except ValueError:
            print("Invalid input. Try again")
    return pick

# Get the computer's pick
def get_computer_pick():
    possible_picks = [1,2,3]
    computer_pick = random.choice(possible_picks)
    pick = Pick(int(computer_pick))
    return pick

# Change the pick's integer value to a string
def to_string(pick_int):
    if (pick_int == Pick.Rock):
        return "Rock"
    elif (pick_int == Pick.Paper):
        return "Paper"
    else:
        return "Scissors"

# Prints the scoreboard
def printScoreboard():
    print("Score: You %d - %d Computer" % (player_score, computer_score))

# Determine who is the winner
def determine_winner(player_pick, computer_pick):
    wins = {Pick.Rock : [Pick.Scissors],    # Rock beats Scissors
            Pick.Paper : [Pick.Rock],       # Paper beats Rock
            Pick.Scissors : [Pick.Paper]}   # Scissors beats Paper
    losses = wins[player_pick]
    print("You chose %s. Computer chose %s." % (to_string(player_pick), to_string(computer_pick)))
    if (player_pick == computer_pick):
        print("It's a tie! Go again")
        return determine_winner(get_player_pick(), get_computer_pick())
    elif (computer_pick in losses):
        print("%s beats %s, so you get a point!\n" % (to_string(player_pick), to_string(computer_pick)))
        return "Player"
    else:
        print("%s beats %s, so the computer gets a point!\n" % (to_string(computer_pick), to_string(player_pick)))
        return "Computer"

# Rules
print("Rules:\n1) Rock beats Scissors\n2) Paper beats Rock\n3) Scissors beat Paper\n4) If there is a tie, continue playing until there is a winner\n5) Best out of 7 rounds wins (First to 4 wins)\n")

# Set up the game
while True:
    player_score = 0
    computer_score = 0
    round_number = 1
    
    # Play the rounds
    for round_number in range(1,8): # Starting at round #1 --> max of 7 rounds'
        print("Round: %d" % round_number)
        printScoreboard()
        winner = determine_winner(get_player_pick(), get_computer_pick())
        
        # Update the score
        if (winner == "Player"):
            player_score += 1
        else:
            computer_score += 1
        
        # Check if there is a winner
        if (player_score == 4):
            print("Game over! You won!")
            printScoreboard()
            break
        elif (computer_score == 4):
            print("Game over! The computer won!")
            printScoreboard()
            break
            
    # Ask to play again
    play_again = input("Would you like to play again?: Y/N\n")
    if (play_again.lower() == 'y' or play_again.lower() == 'yes'):
        continue
    else:
        break
print("Thanks for playing!\n")

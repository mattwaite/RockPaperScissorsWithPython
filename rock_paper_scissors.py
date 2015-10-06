import random #We'll need this later

# First we need a list of all the moves you can make

choices = ["Rock", "Paper", "Scissors"]

# Second, we'll need a simple function that just randomly chooses one of the moves from a the list we created

def choice():
    selection = random.choice(choices)
    return selection
    
# Third, we need a means to determine a winner. However, there's a lot of different things that can go on based on the combination. This is a simple, brute force way to do it. There are others.
    
def winner(player1, player2):
    if player1 == player2:
        return "Tie"
    elif player1 == "Rock" and player2 == "Paper":
        result = "Player 2 wins"
    elif player1 == "Rock" and player2 == "Scissors":
        result = "Player 1 wins"
    elif player1 == "Paper" and player2 == "Rock":
        result = "Player 1 wins"
    elif player1 == "Paper" and player2 == "Scissors":
        result = "Player 2 wins"
    elif player1 == "Scissors" and player2 == "Rock":
        result = "Player 2 wins"
    elif player1 == "Scissors" and player2 == "Paper":
        result = "Player 1 wins"
    return result

# Now, if we want to keep track of wins, we can do it simply by creating a variable for each player and make it a count of their wins. Both players start with zero when the game starts. 

player_1_wins = 0
player_2_wins = 0

# Since everyone plays best two out of three, we can create a while loop that plays the game until someone get's two wins.

while player_1_wins != 2 and player_2_wins != 2:
    player_1 = choice()
    player_2 = choice()
    winr = winner(player_1, player_2)
    print "Player 1 plays %s" % player_1
    print "Player 2 plays %s" % player_2 
    print winr
    # Here's where we'll overwrite the counts of the wins to determine best two of three
    if winr == "Player 1 wins":
        player_1_wins += 1
        print "Player 1 total wins: %i" % player_1_wins
    elif winr == "Player 2 wins":
        player_2_wins += 1 
        print "Player 2 total wins: %i" % player_2_wins
    else:
        pass

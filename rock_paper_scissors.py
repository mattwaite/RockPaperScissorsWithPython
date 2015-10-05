import random

choices = ["Rock", "Paper", "Scissors"]

def choice():
    selection = random.choice(choices)
    return selection
    
def winner(player1, player2):
    if player1 == "Rock" and player2 == "Rock":
        result = "Tie"
    elif player1 == "Rock" and player2 == "Paper":
        result = "Player 2 wins"
    elif player1 == "Rock" and player2 == "Scissors":
        result = "Player 1 wins"
    elif player1 == "Paper" and player2 == "Paper":
        result = "Tie"
    elif player1 == "Paper" and player2 == "Rock":
        result = "Player 1 wins"
    elif player1 == "Paper" and player2 == "Scissors":
        result = "Player 2 wins"
    elif player1 == "Scissors" and player2 == "Scissors":
        result = "Tie"
    elif player1 == "Scissors" and player2 == "Rock":
        result = "Player 2 wins"
    elif player1 == "Scissors" and player2 == "Paper":
        result = "Player 1 wins"
    return result

player_1_wins = 0
player_2_wins = 0

while player_1_wins != 2 and player_2_wins != 2:
    player_1 = choice()
    player_2 = choice()
    winr = winner(player_1, player_2)
    print "Player 1 plays %s" % player_1
    print "Player 2 plays %s" % player_2 
    print winr
    if winr == "Player 1 wins":
        player_1_wins = player_1_wins + 1
        print "Player 1 total wins: %i" % player_1_wins
    elif winr == "Player 2 wins":
        player_2_wins = player_2_wins + 1 
        print "Player 2 total wins: %i" % player_2_wins
    else:
        pass
    
#Pig game - in here we ask PLAYER to roll the dice as per their wish - and can can have as many chances provided 
# and subsequent dice value will be added to score exceot when for dice rolled is 1 then the score is reset to 0 
#if they reaches score of 50 player WINS

import random 
max_score=50
player_scores = []

def rolling():
  return random.randint(1,6)



while True:
    players = input("Input the number of players (2-4) :")
    if players.isdigit():
        players=int(players)
        if 2<= players <= 4:
            break
        else:
            print("player number must be between (2,4)")
            
    else:
        print("Invalid input !!!")



player_scores = [0 for _ in range(players)]

players_idx = 0
while max(player_scores) < max_score:
    for players_idx in range(players):
        print("Player number",players_idx + 1 ,"turn has just started")
        print("Your totla score is ",player_scores[players_idx])
        current_score = 0
        while True:
            roll=input("do you want to roll the dice Y ?").lower()
            if roll != 'y':
                break

            value = rolling()
            if value == 1:
                print("You rolled 1 ! turn done")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a :",value) 

            print("Your score is :",current_score)
        player_scores[players_idx] += current_score
        print("Your total score is :",player_scores[players_idx])

max_score =max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number",winning_idx+1,"is the winnier ")

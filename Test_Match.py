from models.matches import Match
import random

# List and shuffle players
players = ["RY03677", "DP10300", "PB43166", "YQ88272", "RI14529", "AV07547", "OU52460", "CF24301"]
random.shuffle(players)
print(players)

# Set up matches for players
for player in players:
    match = Match(player)
    print(match)

print(match.completed)
print(match.winner)






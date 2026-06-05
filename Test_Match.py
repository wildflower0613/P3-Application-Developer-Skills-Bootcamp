from models.matches import Match
import random


players = ["RY03677", "DP10300", "PB43166", "YQ88272", "RI14529", "AV07547", "OU52460", "CF24301"]
random.shuffle(players)



match = Match(players)
print(match)
print(match.completed)
print(match.winner)






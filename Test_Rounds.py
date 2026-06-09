from models.matches import Match
from models.rounds import Round

players = ["RY03677", "DP10300", "PB43166", "YQ88272", "RI14529", "AV07547", "OU52460", "CF24301"]
round1 = Round(1)
match1 = Match(players)


print(match1)
round1.add_match(match1)
print(round1.matches)


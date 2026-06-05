from models.matches import Match
from models.rounds import Round

round1 = Round(1)
match1 = Match(["shane", "ilia"])
match2 = Match(["RY03677", "DP10300"])


print(match1)
round1.add_match(match1)
print(round1.matches)

print(match2)
round1.add_match(match2)
print(round1.matches)
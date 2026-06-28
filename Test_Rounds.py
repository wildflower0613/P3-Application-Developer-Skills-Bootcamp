from models.matches import Match
from models.rounds import Round

players = ["alice", "bob", "charlie", "david"]
round1 = Round(1)
match1 = Match(players)


print(match1)
round1.add_match(match1)
print(round1.matches)


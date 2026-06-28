from models.tournaments import Tournament
from models.rounds import Round
from models.matches import Match
from models.player import Player

alice = Player("alice", "alice@test.com", "AL12345", "01-01-1990")
bob = Player("bob", "t@y.vu", "NG39713", "29-08-1957")
sarah = Player("sarah", "hortmelvin@example.net", "JW63361", "23-01-1921")
erick = Player(" erick",  "zbyrd@example.net",  "QZ98880", "05-08-1916")

Spring_Tournament = Tournament("Spring_Open", "Chestfall", "06-12-2026", "06-13-2026", 4, 0, False)

print(Spring_Tournament.players)

for player in [alice, bob, sarah, erick]:
    Spring_Tournament.register_players(player)

for player in Spring_Tournament.players:
    print(player)

round1 = Round(1)

match1 = Match([alice, bob])
match2= Match([sarah, erick])


round1.add_match(match1)
round1.add_match(match2)

Spring_Tournament.rounds.append(round1)

match1.set_winner(alice)
match2.set_tie()

print("Points:")
print("alice:", Spring_Tournament.get_points(alice))
print("bob:", Spring_Tournament.get_points(bob))
print("sarah:", Spring_Tournament.get_points(sarah))
print("erick:", Spring_Tournament.get_points(erick))


print("Rankings:")
for player in Spring_Tournament.get_ranks():
    print(player, Spring_Tournament.get_points(player))

print("Played pairs:")
print(Spring_Tournament.get_played_pairs())

for pair in Spring_Tournament.get_played_pairs():
    print([player.name for player in pair])

Summer_Tournament = Tournament("Spring_Open", "Chestfall", "06-12-2026", "06-13-2026", 4, 0, False)

for player in [alice, bob, sarah, erick]:
    Summer_Tournament.register_players(player)
Summer_Tournament.pair_players_for_first_round()

print("Round generation")

for match in Summer_Tournament.rounds[0].matches:
    print(match)
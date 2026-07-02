from models.tournaments import Tournament
from models.rounds import Round
from models.matches import Match
from models.player import Player

alice = Player("alice", "alice@test.com", "AL12345", "01-01-1990")
bob = Player("bob", "t@y.vu", "NG39713", "29-08-1957")
sarah = Player("sarah", "hortmelvin@example.net", "JW63361", "23-01-1921")
erick = Player(" erick",  "zbyrd@example.net",  "QZ98880", "05-08-1916")
teresa = Player("teresa", "teresa@test.com", "TL13345", "03-09-1993")
alex = Player("alex", "alex12@test.com","AX88901", "12-04-1992" )

Spring_Tournament = Tournament("Spring_Open", "Chestfall", "06-12-2026", "06-13-2026", 4, 0, False)

print(Spring_Tournament.players)

for player in [alice, bob, sarah, erick, teresa, alex]:
    Spring_Tournament.register_players(player)

Spring_Tournament.pair_players_for_first_round()
print("Round1_matches")
for match in Spring_Tournament.rounds[0].matches:
    match.set_tie()

Spring_Tournament.generate_next_round()
print("Round2_matches")
for match in Spring_Tournament.rounds[1].matches:
    print(match)



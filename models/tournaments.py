import random
import backtrack
from models.matches import Match
from models.rounds import Round

class Tournament:
    def __init__(self, name, venue, start_date, end_date, number_of_rounds, current_round, completed):
        self.name = name
        self.venue = venue
        self.start_date = start_date
        self.end_date = end_date
        self.players = []
        self.rounds = []
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        self.completed = completed

    def register_players(self, player):
        self.players.append(player)




 # Rounds amd Matchmaking
    def get_points(self, player):
        points = 0.0
            for match in round_.matches:
                if not match.completed :
                    continue
                if match.tie and player in match.players :
                    points += 0.5
                elif match.winner is not None and match.winner == player:
                    points += 1.0
        return points

# Players for 1st round

    def pair_players_for_first_round(self, players):
        round_1= Round(1)
        for round_1 in self.rounds:
            random.shuffle(players)
            print (players.match)

# Players for subsequent rounds
    def countPlayers(self):
        return len(self.players)

    def get_ranks(self):
        return sorted(self.players, key=self.get_points, reverse=True)

    def get_played_pairs(self):
        pairs = set()
        for round_ in self.rounds:
            for match in round_.matches:
                pairs.add(frozenset(match.players))
        return pairs

    def swissPairings(self):
        sorted_players = self.get_ranks()
        played_pairs = self.get_played_pairs()


        numPlayers = countPlayers(name)
        if numPlayers % 2 != 0:
            bye = ranks.pop(checkByes(name, ranks, -1))
            reportBye(name, bye[0])

        while len(ranks) > 1:
            validMatch = checkPairs(name, ranks, 0, 1)
            player1 = ranks.pop(0)
            player2 = ranks.pop(validMatch - 1)
            pairs.append((player1[0], player1[1], player2[0], player2[1]))

        return pairs




















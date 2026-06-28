import random
from models.rounds import Round
from models.matches import Match
from models.player import Player

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
        for round_ in self.rounds:
            for match in round_.matches:
                if not match.completed :
                    continue
                if match.tie and player in match.players :
                    points += 0.5
                elif match.winner is not None and match.winner == player:
                    points += 1.0
        return points

# Players for 1st round

    def pair_players_for_first_round(self):
        shuffled = self.players.copy()
        random.shuffle(shuffled)
        pairs = list(zip(shuffled[::2], shuffled[1::2]))
        round_ = Round(1)
        for pair in pairs:
            match = Match([pair[0], pair[1]])
            round_.add_match(match)
        self.rounds.append(round_)
        self.current_round = 1

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

    def get_players_for_next_rounds(self):
        sort_players = sorted(self, key=self.get_ranks, reverse=True)
        new_matches = sort_players
        for round_ in self.rounds:
            round_.add_match(new_matches)
        return new_matches

#advance rounds (have round update automatically in tournament

    def advance_round(self):
        self.current_round += 1
        return current_round
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
        sort_players = sorted(self.players, key=self.get_points, reverse=True)
        next_round_matches = []
        num_players = len(sort_players)
        if num_players % 2 != 0:
            print (f"Bye awarded to: {num_players[0][0]}")
            sort_players = sort_players[1:]
            num_players = len(sort_players)

        mid_point = num_players // 2
        top_half = sort_players[:mid_point]
        bottom_half = sort_players[mid_point:]

        for i in range (mid_point):
            player1 = top_half[i]
            player2 = bottom_half[-(i+1)]
            next_round_matches.append((player1, player2))
        return next_round_matches

#advance rounds (have round update automatically in tournament

    def advance_round(self):
        self.current_round += 1
        return current_round

    def generate_next_round(self):
        pairs = self.get_players_for_next_rounds()
        round_number = self.current_round+1
        round_ = Round(round_number)
        for pair in pairs:
            match = Match([pair[0], pair[1]])
            round_.add_match(match)
        self.rounds.append(round_)
        self.current_round = round_number

import random
from .matches import Match
from .rounds import Round

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

    def pair_players_for_first_round(self, players):
        for Round(1) in self.rounds:
        random.shuffle(players)

    def pairing_for_swiss_rounds(self, points, players, history):
        self.history = []
        players_to_pair.sort(key=lambda p: points[p], reverse=True)

        def backtrack(remaining_players):
            if not remaining_players:
                return []

            p1 = remaining_players[0]
            for i in range(1, len(remaining_players)):
                p2 = remaining_players[i]

                if p2 not in history.get(p1, set ()):

                    matchup = (p1, p2)

                    next_remaining = remaining[1:i] + remaining[i + 1:]
                    result = backtrack(next_remaining)

                    if result is not None:
                        return [matchup] + result
        return None
    pairings = backtrack(players_to_pair)
    return pairings


















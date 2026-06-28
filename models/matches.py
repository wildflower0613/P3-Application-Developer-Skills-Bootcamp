class Match:
    def __init__(self, players, completed = False, winner = None, tie = False):
        self.players = list(players)
        self.completed = completed
        self.winner = winner
        self.tie = tie

    def __str__(self):
        return f"{self.players[0]} vs {self.players[1]}"

    def set_winner(self, player):
        if player not in self.players:
            raise ValueError(f"{player} is not in this match.")
        self.winner = player
        self.tie = False
        self.completed = True

    def set_tie(self):
        self.winner = None
        self.tie = True
        self.completed = True


    def set_result(self, result):
        if result == 'win':
            self.points += 1.0
            self.winner = True
        elif result == 'tie':
            self.points += 0.5
            self.tie = True


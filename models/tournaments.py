class Tournament:
    def __init__(self, name, venue, start_date, end_date, players, number_of_rounds, current_round, completed):
        self.name = name
        self.venue = venue
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        self.completed = completed

    # Rounds amd Matchmaking
        # Round 1: Shuffle players at random
        random.shuffle(players)
        print(players)

        # List players in descending order of points
        players.sort(reverse=True)
        print(players)



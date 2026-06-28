from .matches import Match
class Round:
    def __init__(self, number):
        self.number = number
        self.matches = []
        self.completed = False


    def add_match (self, match):
        self.matches.append(match)

    def is_finished(self):
        return all(match.completed for match in self.matches)

    def __str__(self):
        return f"Round {self.number}"



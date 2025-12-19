from game import Game


class User:
    DATA_HEADER = ["username", "games", "wins", "answered_questions", "correct_answers", "correct_answers_per_easy", "correct_answers_per_medium", "correct_answers_per_hard"]

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.games = 0 # Počet začatých her
        self.wins = 0 # Počet výher

        self.answered_questions = 0
        self.correct_answers = 0

        self.correct_answers_per_difficulty = {difficulty: 0 for difficulty in Game.DIFFICULTY_LEVELS}

    def win_rate(self):
        if self.games == 0:
            return 0
        return self.wins / self.games

    def lost_games(self):
        return self.games - self.wins


    def to_dict(self):
        return {
            "username": self.username,
            "games": self.games,
            "wins": self.wins,
            "answered_questions": self.answered_questions,
            "correct_answers": self.correct_answers,
            "correct_answers_per_easy": self.correct_answers_per_difficulty["easy"],
            "correct_answers_per_medium": self.correct_answers_per_difficulty["medium"],
            "correct_answers_per_hard": self.correct_answers_per_difficulty["hard"]
        }


    def __str__(self):
        return f"User(name: {self.username}, Wins: {self.wins}/{self.games}, Questions: {self.correct_answers}/{self.answered_questions})"
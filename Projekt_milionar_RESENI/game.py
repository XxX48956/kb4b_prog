from vars import QUIZ_QUESTIONS_PATH, WINNERS_PATH
import csv
import random
    

def game_loop(user):
    print("Lets begin the game!")
    print("\n")

    game = Game(user)
    game.play()


def get_valid_choice(min_value, max_value):
    msg = f"Choose an option: [{min_value}-{max_value}]"
    while True:
        try:
            print(msg)
            choice = int(input(">:"))
            if min_value <= choice <= max_value:
                return choice
            else:
                print(f"Invalid input. Choose number from {min_value} to {max_value}.")
        except ValueError:
            print(f"Invalid input. Choose number from {min_value} to {max_value}.")


def update_winner_stats(user):
    winners_data = {}

    with open(WINNERS_PATH, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if "," in line:
                username, wins = line.split(",")
                winners_data[username] = int(wins)

    if user.username in winners_data:
        winners_data[user.username] += 1
    else:
        winners_data[user.username] = 1

    user.wins += 1

    with open(WINNERS_PATH, "w", encoding="utf-8") as file:
        for name, win_count in winners_data.items():
            file.write(f"{name},{win_count}\n")


class Question:
    def __init__(self, data):
        self.question_text = data["question"]
        self.correct_answer = data["correct_answer"].lower()
        self.difficulty = data["difficulty"].lower()


class Game:
    QUESTION_COUNT = 3
    DIFFICULTY_LEVELS = ["easy", "medium", "hard"]
    QUESTIONS_PER_LEVEL = round(QUESTION_COUNT / len(DIFFICULTY_LEVELS))
    HINTS_AVAILABLE = ["Call a friend", "Public opinion", "50/50"]
    POSITIVE_RESPONSES = ["y", "yes", "t", "true"]
    NEGATIVE_RESPONSES = ["n", "no", "f", "false"]

    def __init__(self, user):
        self.user = user
        self.current_level_index = 0
        self.correct_answers = 0
        self.hints = self.HINTS_AVAILABLE


    def current_difficulty(self):
        return self.DIFFICULTY_LEVELS[self.current_level_index]


    def load_questions(self):
        try:
            with open(QUIZ_QUESTIONS_PATH, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                all_questions = [Question(line) for line in reader]
                if not all_questions:
                    print("Error: No questions in file.")
                    return []
                return all_questions

        except FileNotFoundError:
            print(f"Error: File with questions '{QUIZ_QUESTIONS_PATH}' not found.")
            return []
        except Exception:
            print(f"Error: An error occurred while reading the file '{QUIZ_QUESTIONS_PATH}'.")
            return []


    def get_random_question(self, questions):
        level_questions = [question for question in questions if question.difficulty == self.current_difficulty()]
        
        if not level_questions:
            print(f"Warning: No questions found for difficulty '{self.current_difficulty()}'.")
            return None 
            
        return random.choice(level_questions)


    def update_difficulty(self):
        if self.correct_answers != 0 and self.correct_answers % self.QUESTIONS_PER_LEVEL == 0:
            if self.current_level_index < len(self.DIFFICULTY_LEVELS) - 1:
                self.current_level_index += 1
                print(f"\n New difficulty: **{self.current_difficulty().upper()}**! ")


    def valid_response(self, response, correct_answer):
        if correct_answer == "true":
            if response.lower() in self.POSITIVE_RESPONSES:
                return True
            elif response.lower() in self.NEGATIVE_RESPONSES:
                return False
            else:
                return None
        elif correct_answer == "false":
            if response.lower() in self.NEGATIVE_RESPONSES:
                return True
            elif response.lower() in self.POSITIVE_RESPONSES:
                return False
            else:
                return None


    def call_a_friend(self):
        print(f"\nCall a friend? Sure… if you actually had a friend to call.")


    def public_opinion(self):
        print(f"\nPublic opinion? Great… too bad no one is listening.")


    def fifty_fifty(self):
        print(f"\n50/50? Sure, a hint worthy of a strategy master.")


    def get_hint(self):
        print(f"\nAvailable hints: ")
        
        for index, hint in enumerate(self.hints):
            print(f"[{index + 1}] {hint}")

        hint_choice = get_valid_choice(1, len(self.hints))

        if self.hints[hint_choice - 1] == "Call a friend":
            self.call_a_friend()
            self.hints.pop(hint_choice - 1)
        elif self.hints[hint_choice - 1] == "Public opinion":
            self.public_opinion()
            self.hints.pop(hint_choice - 1)
        elif self.hints[hint_choice - 1] == "50/50":
            self.fifty_fifty()
            self.hints.pop(hint_choice - 1)
        else:
            return


    def get_response(self):
        while True:
            response = input("Your answer: ").strip().lower()
            if response in self.POSITIVE_RESPONSES or response in self.NEGATIVE_RESPONSES:
                return response
            elif response == "hint":
                self.get_hint()
            elif response == "quit":
                return "quit"
            else:
                print("Invalid response. Please enter 'y' for yes, 'n' for no, 'hint' for a hint, or 'quit' to exit the game.") 


    def ask_question(self, question):
        print(f"\n--- Question number {self.correct_answers + 1} ({self.current_difficulty()}) ---")
        print(f"Question: {question.question_text}")
        
        print(f"\nRemaining hints: ['hint']\n\t{', '.join(self.hints) if self.hints else 'None'}")
        
        response = self.get_response()
        if response == "quit":
            return None
            
        is_correct = self.valid_response(response, question.correct_answer)
        
        if is_correct:
            print("Correct answer.")
        else:
            print(f"Wrong answer. The correct answer is **{question.correct_answer}**.")
            return None
            
        return is_correct


    def play(self):
        print("Game begins! Good luck!")
        
        questions = self.load_questions() # Initialization
        if not questions:
            return

        while self.correct_answers < self.QUESTION_COUNT:
            self.update_difficulty() # Difficulty check before question
            
            current_question = self.get_random_question(questions)
            if not current_question:
                print("Error: No questions available.")
                break

            questions.remove(current_question) # Exclude used question

            if self.ask_question(current_question): # Question check
                self.correct_answers += 1
            else:
                print(f"\n**GAME OVER!** Wrong answer. You got {self.correct_answers} correct answers.")
                return

        if self.correct_answers == self.QUESTION_COUNT:
            print(f"\n **Congratulation!**")
            print(f"You have answered all {self.QUESTION_COUNT} questions correctly and won the game!**")

            update_winner_stats(self.user) # Update winner stats


def display_rules():
    print("\nGame Rules: ")
    print(f"You have to correctly answer {Game.QUESTION_COUNT} questions to win the game.")
    print(f"Every series of {Game.QUESTIONS_PER_LEVEL} questions will increase the difficulty.")
    print("You have just one chance: one wrong answer and game ends.")
    print(f"You can also use {len(Game.HINTS_AVAILABLE)} hints: {', '.join(Game.HINTS_AVAILABLE)}.")
    print()

def display_hints():
    print("\nHints: ")
    for hint in Game.HINTS_AVAILABLE:
        print(f"- {hint}")
    print()



def game_introduction(user):
    print(f"Welcome, {user.username}!")
    print("Let's play the čichna millionaire game.")
    print(f"You have to answer {Game.QUESTION_COUNT} questions.")
    print(f"With every serie of questions difficulty will increase.")
    print("You have only one chance, one wrong answer and its over.")
    print("Good luck!")
    print("\n")


def game_main_menu(user):
    game_introduction(user)

    while True:    
        print("Game Menu")
        print("[1] Play")
        print("[2] Rules")
        print("[3] Hints")
        print("[4] Exit")

        choice = get_valid_choice(1, 4)
        
        if choice == 1:
            game = Game(user)
            game.play()
        elif choice == 2:
            display_rules()
        elif choice == 3:
            display_hints()
        elif choice == 4:
            break
        else:
            print("Error: Invalid choice.")



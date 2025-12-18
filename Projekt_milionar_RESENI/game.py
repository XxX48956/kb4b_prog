from csv import DictReader
from random import choice
from vars import QUIZ_QUESTIONS_PATH, WINNERS_PATH
from winners import update_winner_stats
    

def get_valid_choice(min_value, max_value):
    while True:
        try:
            print(f"Choose an option: [{min_value}-{max_value}]")
            choice = int(input(">:"))
            if min_value <= choice <= max_value:
                return choice
            else:
                print(f"Invalid input. Choose number from {min_value} to {max_value}.")
        except ValueError:
            print(f"Invalid input. Choose number from {min_value} to {max_value}.")


class Question:
    def __init__(self, data):
        self.question_text = data["question"]
        self.correct_answer = data["correct_answer"].strip().lower
        self.difficulty = data["difficulty"].strip().lower


class Game:
    QUESTION_COUNT = 15
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


    def load_all_questions(self, path = QUIZ_QUESTIONS_PATH):
        try:
            with open(path, "r", encoding="utf-8") as file:
                return [Question(line) for line in DictReader(file)] 

        except FileNotFoundError:
            print(f"Error: File with questions '{path}' not found.")
            return []


    def get_random_question(self, questions):
        level_questions = [question for question in questions if question.difficulty == self.current_difficulty()]
        
        if not level_questions:
            print(f"Warning: No questions found for difficulty '{self.current_difficulty()}'.")
            return None 
            
        return choice(level_questions)


    def update_difficulty(self):
        if self.correct_answers != 0 and self.correct_answers % self.QUESTIONS_PER_LEVEL == 0:
            if self.current_level_index < len(self.DIFFICULTY_LEVELS) - 1:
                self.current_level_index += 1
                print(f"\n New difficulty: **{self.current_difficulty().upper()}**! ")


    def check_answer(self, response, correct_answer):
        if correct_answer in self.POSITIVE_RESPONSES:
            return response in self.POSITIVE_RESPONSES
        if correct_answer in self.NEGATIVE_RESPONSES:
            return response in self.NEGATIVE_RESPONSES
        return response == correct_answer
    

    def use_hint(self):
        if not self.hints:
            print("\nNo more hints")
            return

        print("\n--- Available hints ---")
        for index, hint in enumerate(self.hints, 1):
            print(f"[{index}] {hint}")
        
        choice = get_valid_choice(1, len(self.hints)) - 1
        selected_hint = self.hints.pop(choice)

        messages = {
            "Call a friend": "Call a friend? Sure… if you actually had a friend to call.",
            "Public opinion": "Public opinion? Great… too bad no one is listening.",
            "50/50": "50/50? Sure, a hint worthy of a strategy master."
        }

        if selected_hint in messages:
            print(f"\n{messages[selected_hint]}")
        else:
            print("Hint not found.")


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
        while True:
            response = input("Your answer: [or 'hint' / 'quit']").strip().lower()

            if response in ['quit', 'q', 'exit', 'e']:
                return False

            if response in ['h', 'hint', 'hints']:
                self.use_hint()
                print(f"\n Question: {question.question_text}")
                continue

            if response in self.POSITIVE_RESPONSES or response in self.NEGATIVE_RESPONSES:
                is_correct = self.check_answer(response, question.correct_answer)
                self.user.answered_questions += 1

                if is_correct:
                    print("Correct answer.")
                    self.user.correct_answers += 1
                    return True
                else:
                    print(f"Wrong answer. The correct answer is **{question.correct_answer}**.")
                    return False

            print("Invalid response. Please enter 'y' for yes, 'n' for no, 'hint' for a hint, or 'quit' to exit the game.")


    def play(self):
        print("--- Game begins! Good luck! ---")
        self.user.games += 1
        questions = self.load_all_questions() # Initialization
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

            self.user.wins += 1
            update_winner_stats(self.user, WINNERS_PATH) # Update winner stats


def game_introduction(user):
    print(f"Welcome, {user.username}!")
    print("Let's play the čichna millionaire game.")
    print(f"You have to answer {Game.QUESTION_COUNT} questions.")
    print(f"With every serie of questions difficulty will increase.")
    print("You have only one chance, one wrong answer and its over.")
    print("Good luck!")
    print("\n")


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

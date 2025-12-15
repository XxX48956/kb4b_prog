def game(user):
    game_introduction(user) # Přivítání
    choice = start_game_menu() # Potvrzovací menu

    if choice == 1:
        game_loop(user)
    elif choice == 2:
        rules()
    elif choice == 3:
        return
    else:
        print("Error: Invalid choice.")

def game_loop(user):
    print("Lets begin the game!")
    print("\n")

    game = Game(user)
    game.play()


def rules():
    print("Rules: ")
    print("You have to answer 15 questions correctly to win the game.")
    print("Correct answer => +1 level")
    print("Wrong answer => you lose")
    print("No Cheating! Just your brain!")
    print("You have 3 hints.")
    print("Write your answer as [y/n] or [yes/no] or [t/f] or [true/false].")
    print("\n")


def hints():
    print("Hints")
    print("Call a friend.")
    print("Public opinion.")
    print("50/50.")
    print("\n")

def game_introduction(user):
    print(f"Welcome, {user.username}!")
    print("Let's play the čichna millionaire game!")
    print("You have to answer 15 questions correctly to win the game.")
    print("Do not worry you have 3 hints.")
    print("But every 5 question difficulty will increase.")
    print("You have only one oppertunity, one wrong answer and its over.")
    print("Good luck!")
    print("\n")


def start_game_menu():
    while True:    
        print("Game Menu")
        print("[1] Play")
        print("[2] Rules")
        print("[3] Exit")
        
        try:
            print("Choose option [1-3]:")
            choice = int(input(">:"))
            if choice <= 1 or choice >= 3:
                return choice
            else:
                print("Invalid input. Choose number from 1 to 3.")
        except ValueError:
            print("Invalid input. Choose number from 1 to 3.")


class Game:
    def __init__(self, user):
        self.user = user
        self.level = "easy"
        self.score = 0
        self.money = 0
        self.hints = ["Call a friend", "Public opinion", "50/50"]
        self.levels = ["easy", "medium", "hard"]

    def play(self):
        pass
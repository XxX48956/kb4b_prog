USERS = []
EXIT = False
QUIZ_QUESTIONS_PATH = r"Projekt_milionar_RESENI\files\quiz_questions.csv"
AUTH_PATH = r"Projekt_milionar_RESENI\files\users.txt"
WINNERS_PATH = r"Projekt_milionar_RESENI\files\winners.txt"

def end():
    choice = input("End App? [y/n]")
    if choice == "y":
        print("Goodbye!")
        vars.EXIT = True

exit = False
users = []
quizQuestionsPath = "Projekt_milionar_RESENI\files\quiz_questions.csv"
authPath = "Projekt_milionar_RESENI\files\users.txt"
winnersPath = "Projekt_milionar_RESENI\files\winners.txt"

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register_to_txt(self):
        with open(authPath, "a", encoding="utf-8") as file:
            file.write(f"{self.username}: {self.password}")


    def __del__(self):
        print(f"Objekt se jmenem {self.username} byl smazán")


def main():
    isAuth = auth()
    while not exit:
        print("")


def login():
    print("Login:")
    while not exit:
        pass


def register():
    print("Registration:")
    username = input("Enter your username: \n>:")
    password = input("Enter your password: \n>:")
    users.append(User(username, password))

    
# def registration_to_txt(username, password):
#     with open(authPath, "a", encoding="utf-8") as file:
#         file.write(f"{username}: {password}")

def auth():
    choice = authMenu()
    if choice == 1:
        return login()
    elif choice == 2:
        return register()
    elif choice == 3:
        exit = True
    else:
        print("Invalid choice. \nChoose in range 1-3")
        authMenu()


def authMenu():
    while not exit:
        print("User Authentication Menu")
        print("[1] Login")
        print("[2] Register")
        print("[3] Exit")

        try:
            choice = int(input(">:"))
        except:
          print("Invalid input. \nChoose number 1-3")
        
        return choice





class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.register_to_txt()

    def register_to_txt(self):
        with open(authPath, "a", encoding="utf-8") as file:
            file.write(f"{self.username}: {self.password}\n")


    def __del__(self):
        print(f"Objekt se jménem {self.username} byl smazán")


def login():
    print("Login:")
    while not exit:
        pass

def username_txt_check(username):
    # Kontrola existujícího uživatelského jména
    with open(authPath, "r", encoding="utf-8") as file:
        existing_users = [line.split(": ")[0] for line in file.readlines()]

    if username in existing_users:
        print("Uživatelské jméno již existuje! Zkuste jiné.")
        return False  
    return True 


def register():
    print("Registration:")
    username = input("Enter your username: \n>:")

    if not username_txt_check(username):
        return False

    password = input("Enter your password: \n>:")
    users.append(User(username, password))
    
    print(f"Uživatel {username} byl úspěšně zaregistrován.")
    return True
    

    

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
        return auth()


def authMenu():
    print("User Authentication Menu")
    
    while 1:
        print("[1] Login")
        print("[2] Register")
        print("[3] Exit")

        try:
            choice = int(input(">:"))
        except:
          print("Invalid input. \nChoose number 1-3")
        
        return choice






def load_users(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("Authentication file not found.")
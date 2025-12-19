from vars import AUTH_PATH
from user import User


def parse_credentials_line(line): # 2 parts from file line, split USERNAME, PASSWORD
    cleaned_line = line.strip()
    if not cleaned_line:
        return None  # Skip empty lines

    parts = cleaned_line.split(": ", maxsplit=1) # Split the line in first match
    
    if len(parts) == 2 and all(parts):
        return parts[0], parts[1]

    return None
        

def find_user_credentials_in_file(username, password, path = AUTH_PATH): # Authenticate User with TXT file
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                credentials = parse_credentials_line(line)
                
                if credentials:
                    file_username, file_password = credentials
                    # Porovnání uživatelského jména a hesla
                    if file_username == username and file_password == password:
                        return True
        return False
    except FileNotFoundError:
        print(f"Error: Auth File not found on path: {path}")
        return False


def find_user_in_object_list(username, password, user_map): # Find adn return user object
    if username in user_map and user_map[username].password == password:
        return user_map[username]
    return None


def is_quiting(input): # Check for 'q' command
    return input.strip().lower() in ("q", "quit", "e", "exit")


def get_login_input():
    print("\nLogin: (Enter 'q' to quit)")

    username = input("Enter your username: \n>:").strip()
    if is_quiting(username): 
        return "exit"

    password = input("Enter your password: \n>:").strip()
    if is_quiting(password):
        return "exit"

    return username, password


def authentization_login_loop():
    while True:
        # --- 1 ---
        inputs = get_login_input()
        
        # --- 2 ---
        if inputs == "exit":
            return None
        
        username, password = inputs
        
        # --- 3 ---
        if not username or not password:
            print("Error: Please enter both username and password.")

        # --- 4 ---
        is_authenticated = find_user_credentials_in_file(username, password, AUTH_PATH)
        if is_authenticated:
            return username, password

        # --- 5 ---
        if not is_authenticated:
            print("Error: Invalid username or password.")


def login(user_map):
    # 1. Získá vstupy.
    # 2. Zkontroluje přítomnost příkazu pro ukončení.
    # 3. Ověří že byly zadány údaje
    # 4. Ověří přihlašovací údaje ze souboru a určí stav (auth).
    # 5. Zkontroluje stav
    # 6. Najde odpovídající uživatelský objekt.
    # 7. Zkontroluje a vrátí objekt
    
    credentials = authentization_login_loop()
    if credentials:
        username, password = credentials
    else:
        return None
    
    # --- 6 ---
    user_object = find_user_in_object_list(username, password, user_map)
    
    # --- 7 ---
    if user_object:
        print(f"Welcome back, {user_object.username}!")
        return user_object
    else: 
        print("Error: User object not found.")
        return None
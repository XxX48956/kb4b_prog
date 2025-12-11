import vars
from user import User


def parse_credentials_line(line):
    cleaned_line = line.strip()
    if not cleaned_line:
        return None  # Skip empty lines

    parts = cleaned_line.split(": ", maxsplit=1) # Split the line in first match
    
    if len(parts) == 2 and all(parts):
        return parts[0], parts[1]

    return None

def find_user_credentials_in_file(file_path, username, password):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                credentials = parse_credentials_line(line)
                
                if credentials:
                    file_username, file_password = credentials
                    # Porovnání uživatelského jména a hesla
                    if file_username == username and file_password == password:
                        return True
        return False
    except FileNotFoundError:
        print(f"Error: Auth File not found on path: {file_path}")
        return False


def find_user_in_object_list(username, password, user_list):
    for user in user_list:
        # POUZE pokud třída User má atributy username a password
        if user.username == username and user.password == password:
            return user
    return None

def check_for_quit_command(username_input, password_input):
    if username_input.lower() == "q" or password_input.lower() == "q":
        vars.EXIT = True
        return True
    return False

def get_login_input():
    print("\nLogin: (Enter 'q' to quit)")
    username = input("Enter your username: \n>:").strip()
    password = input("Enter your password: \n>:").strip()

    return username, password


def login():
    
    # 1. Získá vstupy.
    # 2. Zkontroluje příkaz pro ukončení.
    # 3. Ověří přihlašovací údaje ze souboru.
    # 4. Vyhledá odpovídající objekt uživatele.
    
    username, password = get_login_input()
    
    if check_for_quit_command(username, password):
        return None

    if not username or not password:
        print("Error: Please enter both username and password.")
        return None

    is_authenticated = find_user_credentials_in_file(vars.AUTH_PATH, username, password)
    
    if not is_authenticated:
        print("Error: Invalid username or password.")
        return None

    user_object = find_user_in_object_list(username, password, vars.USERS)
        
    if user_object:
        print(f"Welcome back, {user_object.username}!")
        return user_object
    else: 
        print("Error: User object not found.")
        return None

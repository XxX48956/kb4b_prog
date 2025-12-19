from user import User
from vars import AUTH_PATH


def is_username_available_file(username, path = AUTH_PATH): # Check file if username is available
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    existing_user = line.split(": ", maxsplit=1)[0]
                    if existing_user == username:
                        return False
            return True

    except FileNotFoundError:
        print(f"Error: Auth File not found on path: {path}")
        return True


def is_quiting(input): # Check for 'q' command
    return input.strip().lower() in ("q", "quit", "e", "exit")


def username_registration_loop():
    while True:
        username = input("Enter your username: \n>:").strip()
        
        if is_quiting(username):
            return "exit"
        
        if is_username_available_file(username, AUTH_PATH):
            return username
        
        print("Username is already taken. Choose different one.")


def password_validation(length = 4):
    while True:
        password = input("Enter new password: \n>:").strip()

        if is_quiting(password):
            return "exit"
        
        if len(password) >= length:
            return password
        
        print(f"Password is too short. Must be at least {length} characters.")


def save_auth_to_file(username, password, path = AUTH_PATH):
    try:
        with open(path, "a", encoding="utf-8") as file:
            file.write(f"{username}: {password}\n")
    
    except FileNotFoundError:
        print(f"Error: Auth File not found on path: {path}")


def register(user_map):
    print("\nRegistration: (Enter 'q' to quit))")

    username = username_registration_loop()    
    if username == "exit":
        return None

    password = password_validation()
    if password == "exit":
        return None

    new_user = User(username, password)
    user_map[username] = new_user
    save_auth_to_file(username, password, AUTH_PATH)
    
    print(f"Successfull registration {username}")
    return new_user
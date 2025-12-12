from user import User
from vars import USERS, AUTH_PATH


def is_username_available_file(path, username): # Check file if username is available
    with open(path, "r", encoding="utf-8") as file:
        existing_users = [line.split(": ")[0] for line in file.readlines()]

    return username not in existing_users


def is_quiting(input): # Check for 'q' command
    if input.lower() == "q":
        return True
    return False


def username_registration_loop():
    while True:
        username = input("Enter your username: \n>:").strip()
        
        if is_quiting(username):
            return "exit"
        
        if is_username_available_file(AUTH_PATH, username):
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


def save_auth_to_file(path, username, password):
        with open(path, "a", encoding="utf-8") as file:
            file.write(f"{username}: {password}\n")
            file.close()


def register():
    print("\nRegistration: (Enter 'q' to quit))")

    username = username_registration_loop()
    
    if username == "exit":
        return None
    password = password_validation()
    if password == "exit":
        return None

    new_user = User(username, password)
    USERS.append(new_user)
    save_auth_to_file(AUTH_PATH, username, password)
    
    print(f"Successfull registration {username}")
    return new_user
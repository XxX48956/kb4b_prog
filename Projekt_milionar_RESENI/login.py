import vars
from user import User

def line_validation(line):
    line = line.strip()
    if not line: # Skip empty line
        return None
    
    parts = line.split(": ", maxsplit=1) # Split the line in first match
    if len(parts) == 2: # Check if the line has two parts
        file_username, file_password = parts
        return file_username, file_password

    return None


def login_from_file(path, username, password):
    with open(path, "r", encoding="utf-8") as file:
        for line in file.readlines():
            checked_line = line_validation(line)

            if not checked_line:
                continue

            file_username, file_password = checked_line
            if file_username != username:
                continue

            if file_password == password:
                return file_username, file_password

    return False


def login_from_object(username, password):
    for user in vars.USERS:
        if user.username == username and user.password == password:
            return user

    return None


def login():
    print("Login:")
    username = input("Enter your username: \n>:").strip()
    password = input("Enter your password: \n>:").strip()

    file_username, file_password = login_from_file(vars.AUTH_PATH, username, password)

    if file_username and file_password:        
        user_object = login_from_object(file_username, file_password)
        
        if user_object:
            print(f"Vítejte zpět, {user_object.username}!")
            return user_object
        else: 
            new_user = User(file_username, file_password)
            vars.USERS.append(new_user) 
            
            print(f"Welcome, {new_user.username}! (New object created)")
            return new_user
    else:
        print("Invalid username or password.")
        return None

    
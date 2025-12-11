from vars import USERS
from user import User




def parse_credentials_line(line):
    cleaned_line = line.strip()
    if not cleaned_line:
        return None  # Skip empty lines

    parts = cleaned_line.split(": ", maxsplit=1) # Split the line in first match
    
    if len(parts) == 2 and all(parts):
        return parts[0], parts[1]

    return None

def load_user_objects_from_file(path):
    new_users = []
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                credentials = parse_credentials_line(line)
                
                if credentials:
                    username, password = credentials

                    new_users.append(User(username, password))
                    
    except FileNotFoundError:
        print(f"Error: Auth File not found on path: {path}")
        return []
        
    return new_users

def initialize_user_list():
    loaded_users = load_user_objects_from_file(AUTH_PATH)
    
    USERS.clear()
    USERS.extend(loaded_users)



def recreate_user_objects(path):
    with open(path, "r", encoding="utf-8") as file:
        user_data = []
        for line in file:
                credentials = parse_credentials_line(line)
                
                if credentials:
                    file_username, file_password = credentials
                    USERS.append(User(file_username, file_password))






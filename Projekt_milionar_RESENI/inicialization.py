from vars import AUTH_PATH, USERS_DATA_PATH
from user import User
from csv import DictReader


def parse_credentials_line(line):
    cleaned_line = line.strip()
    if not cleaned_line or ": " not in cleaned_line:
        return None  # Skip empty lines

    parts = cleaned_line.split(": ", maxsplit=1) # Split the line in first match
    
    if len(parts) == 2 and all(parts):
        return parts[0], parts[1]

    return None


def safe_int_value(value):
    if value and value.strip():
        return int(value)
    return 0


def recreate_user_objects(auth_path = AUTH_PATH, users_data_path = USERS_DATA_PATH):
    user_map = {}

    # Vytvoření objektů a uložení do dict z AUTH_FILE
    try:
        with open(auth_path, "r", encoding="utf-8") as file:
            for line in file:
                credentials = parse_credentials_line(line)
                if credentials:
                    file_username, file_password = credentials
                    user_map[file_username] = User(file_username, file_password)
    except FileNotFoundError:
        print(f"Error: Auth File not found on path: {auth_path}")
        return {}

    try:
        with open(users_data_path, "r", encoding="utf-8") as file:
            reader = DictReader(file)

            for line in reader:
                username = line["username"]

                if username in user_map:
                    user = user_map[username]

                    user.games = safe_int_value(line["games"])
                    user.wins = safe_int_value(line["wins"])
                    user.answered_questions = safe_int_value(line["answered_questions"])
                    user.correct_answers = safe_int_value(line["correct_answers"])

                    user.correct_answers_per_difficulty["easy"] = safe_int_value(line["correct_answers_per_easy"])
                    user.correct_answers_per_difficulty["medium"] = safe_int_value(line["correct_answers_per_medium"])
                    user.correct_answers_per_difficulty["hard"] = safe_int_value(line["correct_answers_per_hard"])

    except FileNotFoundError:
        print(f"Error: Users Data File not found on path: {users_data_path}")
        return user_map

    return user_map
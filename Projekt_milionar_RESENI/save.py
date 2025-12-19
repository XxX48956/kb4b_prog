from vars import USERS_DATA_PATH
from user import User
from csv import DictWriter


def save_user_stats(user_map, path = USERS_DATA_PATH, header = User.DATA_HEADER):
    if not user_map:
        return

    if not header:
        header = ["username", "games", "wins", "answered_questions", "correct_answers", "correct_answers_per_easy", "correct_answers_per_medium", "correct_answers_per_hard"]
    try:
        with open(path, "w", encoding="utf-8", newline="") as file:
            writer = DictWriter(file, fieldnames=header)
            writer.writeheader()
            
            # Projdeme všechny uživatele a zapíšeme jejich data
            for user in user_map.values():
                data_to_save = user.to_dict()

                writer.writerow(data_to_save)
        print(f"Stats saved: {path}")
    except FileNotFoundError:
        print(f"Error: File with user data '{path}' not found.")
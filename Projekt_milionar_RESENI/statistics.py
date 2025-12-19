import matplotlib.pyplot as plt
from csv import DictReader
from vars import QUIZ_QUESTIONS_PATH
from game import Game


def get_valid_choice(min_value, max_value):
    while True:
        try:
            print(f"Choose an option: [{min_value}-{max_value}]")
            choice = int(input(">:"))
            if min_value <= choice <= max_value:
                return choice
            else:
                print(f"Invalid input. Choose number from {min_value} to {max_value}.")
        except ValueError:
            print(f"Invalid input. Choose number from {min_value} to {max_value}.")


def draw_bar_chart(data_dict, title, xlabel, ylabel = "Question count", main_value = None):
    if not data_dict:
        print(f"No data for graph '{title}' to draw.")
        return
    
    def sort_by_value(item):
        return item[1]
    # Seřazení dat podle velikosti (od nejvíce otázek po nejméně)
    sorted_data = dict(sorted(data_dict.items(), key=sort_by_value, reverse=True))
    
    names = list(sorted_data.keys())
    values = list(sorted_data.values())

    colors = []

    if main_value:
        for name in names:
            if name == main_value:
                colors.append("green")
            else:
                colors.append("blue")
    else:
        colors = ["blue"] * len(values)

    bars = plt.bar(names, values, color = colors)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.xticks(rotation=45, ha="right")
    plt.grid(axis='y', linestyle='-', alpha=0.4)
    plt.tight_layout()
    plt.show()


def get_correct_answers_per_person(user_map):
    if not user_map:
        return {}

    data = {}
    for user in user_map.values():
        data[user.username] = user.correct_answers

    return data


def get_wins_per_person(user_map):
    if not user_map:
        return {}

    data = {}
    for user in user_map.values():
        data[user.username] = user.wins

    return data


def get_win_rates_per_person(user_map):
    if not user_map:
        return {}

    data = {}
    for user in user_map.values():
        data[user.username] = user.win_rate()

    return data


def get_correct_answers_per_difficulty(user_map):
    if not user_map:
        return {}

    data = {level: 0 for level in Game.DIFFICULTY_LEVELS}

    for user in user_map.values():
        for level, count in user.correct_answers_per_difficulty.items():
            if level in data:
                data[level] += count

    return data


def get_data_from_csv(column_name, path = QUIZ_QUESTIONS_PATH):
    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = DictReader(file)

            data = {}
            for line in reader:
                value = line[column_name]
                if value in data:
                    data[value] += 1
                else:
                    data[value] = 1

            return data

    except FileNotFoundError:
        print(f"Error: File with questions '{path}' not found.")
        return None


def get_grouped_category_stats(path = QUIZ_QUESTIONS_PATH):
    raw_stats = get_data_from_csv("category", path)
    grouped_stats = {}

    for category_name, count in raw_stats.items():
        main_category = category_name.split(": ")[0] if ": " in category_name else category_name

        if main_category in grouped_stats:
            grouped_stats[main_category] += count
        else:
            grouped_stats[main_category] = count

    return grouped_stats


def draw_questions_per_category():
    stats = get_data_from_csv("category")
    draw_bar_chart(stats, "Questions per category", "Category names", "Question count")


def draw_questions_per_grouped_category():
    stats = get_grouped_category_stats()
    draw_bar_chart(stats, "Questions per grouped category", "Grouped categories", "Question count")


def draw_questions_per_difficulty():
    stats = get_data_from_csv("difficulty")
    draw_bar_chart(stats, "Questions per difficulty", "Difficulty", "Question count")


def draw_questions_per_answer():
    stats = get_data_from_csv("correct_answer")
    draw_bar_chart(stats, "Questions per answer", "Answer", "Question count")


def draw_correct_answers_per_person(user_map, user):
    stats = get_correct_answers_per_person(user_map)
    draw_bar_chart(stats, "Correct answers per person", "Person", "Correct answers", main_value=user.username)


def draw_wins_per_person(user_map, user):
    stats = get_wins_per_person(user_map)
    draw_bar_chart(stats, "Wins per person", "Person", "Wins", main_value=user.username)


def draw_win_rates_per_person(user_map, user):
    stats = get_win_rates_per_person(user_map)
    draw_bar_chart(stats, "Win rates per person", "Person", "Win rates", main_value=user.username)


def draw_correct_answers_per_difficulty(user_map):
    stats = get_correct_answers_per_difficulty(user_map)
    draw_bar_chart(stats, "Correct answers per difficulty", "Difficulty", "Correct answers")


def statistics(user_map, user):
    while True:
        print("\nStatistics menu:")
        print("[1] Questions per category")
        print("[2] Questions per grouped category")
        print("[3] Questions per difficulty")
        print("[4] Questions per answer")
        print("[5] Correct answers per person")
        print("[6] Wins per person")
        print("[7] Win rates per person")
        print("[8] Correct answers per difficulty")
        print("[9] Back to main menu")

        choice = get_valid_choice(1, 9)

        if choice == 1:
            draw_questions_per_category()
        
        elif choice == 2:
            draw_questions_per_grouped_category()
        
        elif choice == 3:
            draw_questions_per_difficulty()
        
        elif choice == 4:
            draw_questions_per_answer()

        elif choice == 5:
            draw_correct_answers_per_person(user_map, user)
        
        elif choice == 6:
            draw_wins_per_person(user_map, user)
        
        elif choice == 7:
            draw_win_rates_per_person(user_map, user)

        elif choice == 8:
            draw_correct_answers_per_difficulty(user_map)
        
        elif choice == 9:
            return
        else:
            print("Invalid choice. Please try again.")
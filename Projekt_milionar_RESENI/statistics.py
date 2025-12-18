import matplotlib.pyplot as plt
import csv
from vars import QUIZ_QUESTIONS_PATH

def get_category_names(path):
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        category_names = [line["category"] for line in reader]
        category_names = list(set(category_names))
        return category_names
    
def get_questions_count_by_category(path):
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        names = get_category_names(path)

        values = [0 for name in range(len(names))]
        #values = [0,0,0,0,0,0,0,0,0,0]
        for line in reader:
            for i in range(len(names)):
                if line["category"] == names[i]:
                    values[i] += 1

        return values


def get_difficulty_names(path):
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        difficulty_names = [line["difficulty"] for line in reader]
        difficulty_names = list(set(difficulty_names))
        return difficulty_names


def get_questions_count_by_difficulty(path):
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        names = get_difficulty_names(path)

        values = [0 for name in range(len(names))]
        #values = [0,0,0,0,0,0,0,0,0,0]
        for line in reader:
            for i in range(len(names)):
                if line["difficulty"] == names[i]:
                    values[i] += 1

        return values

#get_questions_count_by_category(QUIZ_QUESTIONS_PATH)


def questions_per_category_stats():
    names = get_category_names(QUIZ_QUESTIONS_PATH)
    values = get_questions_count_by_category(QUIZ_QUESTIONS_PATH)

    plt.bar(names, values)

    plt.title("Category stats")
    plt.xlabel("Category name")
    plt.ylabel("Questions count")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.show()

def questions_per_category_short_stats():
    names = get_category_names(QUIZ_QUESTIONS_PATH)
    short_names = []
    for name in names:
        if ": " in name:
            short_name, _ = name.split(": ")
            short_names.append(short_name)
        else:
            short_names.append(name)

    short_names = list(set(short_names))
    # print(short_names)
    values = get_questions_count_by_category(QUIZ_QUESTIONS_PATH)

    plt.bar(short_names, values)

    plt.title("Category stats")
    plt.xlabel("Category name")
    plt.ylabel("Questions count")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.show()

#questions_per_category_stats()

def questions_per_difficulty_stats():
    names = get_difficulty_names(QUIZ_QUESTIONS_PATH)
    values = get_questions_count_by_difficulty(QUIZ_QUESTIONS_PATH)

    plt.bar(names, values)

    plt.title("Category stats")
    plt.xlabel("Difficulty")
    plt.ylabel("Questions count")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.show()


#questions_per_category_short_stats()

def get_questions_per_category(path, col_name):
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = {}
        names = []
        values = []

        for line in reader:
            if line[col_name] in data:
                data[line[col_name]] += 1
            else:
                data[line[col_name]] = 1

       
        for item in data.items():
            name, count = item
            names.append(name)
            values.append(count)
    return names, values
get_questions_per_category(QUIZ_QUESTIONS_PATH)
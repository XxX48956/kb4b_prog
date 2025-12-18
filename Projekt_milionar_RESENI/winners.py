

def winners_log(path):
    winners_data = {}

    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if not lines:
            print("No winners yet.")
            return None
        
        for line in lines:
            line = line.strip()
            if "," in line:
                username, wins = line.split(",")
                winners_data[username] = int(wins)


        for index, (name, wins) in enumerate(winners_data.items(), start=1):
            print(f"{index}. {name} {wins}x wins")

    return None

def update_winner_stats(user, path):
    winners_data = {}

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if "," in line:
                username, wins = line.split(",")
                winners_data[username] = int(wins)

    if user.username in winners_data:
        winners_data[user.username] += 1
    else:
        winners_data[user.username] = 1

    user.wins += 1

    with open(path, "w", encoding="utf-8") as file:
        for name, win_count in winners_data.items():
            file.write(f"{name},{win_count}\n")

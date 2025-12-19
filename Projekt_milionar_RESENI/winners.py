from vars import WINNERS_PATH


def winners_log(path = WINNERS_PATH):
    winners_data = {}

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if "," in line:
                    username, wins = line.split(",", maxsplit=1)
                    winners_data[username] = int(wins)

            if not winners_data:
                print("No winners yet.")
                return

            print("\n--- Hall of Fame ---")
            for index, (name, wins) in enumerate(winners_data.items(), start=1):
                print(f"{index}. {name}: {wins}x wins")

        return winners_data

    except FileNotFoundError:
        print(f"Error: File with winners '{path}' not found.")
        return None


def update_winner_stats(user, path = WINNERS_PATH):
    winners_data = {}

    try:
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

    except FileNotFoundError:
        print(f"Error: File with winners '{path}' not found.")


    try:
        with open(path, "w", encoding="utf-8") as file:
            for name, win_count in winners_data.items():
                file.write(f"{name},{win_count}\n")
                
    except FileNotFoundError:
        print(f"Error: File with winners '{path}' not found.")
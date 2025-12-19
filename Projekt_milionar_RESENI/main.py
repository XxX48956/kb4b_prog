from auth import auth_loop
from inicialization import recreate_user_objects
from vars import WINNERS_PATH, AUTH_PATH, USERS_DATA_PATH
from game import game_main_menu
from winners import winners_log
from save import save_user_stats
from statistics import statistics
    

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


def main_menu(user, user_map):
    while True:
        print("\n" + "="*20)
        print(f" LOGGED AS: {user.username} ")
        print("="*20)
        print("[1] Play Game")
        print("[2] Statistics")
        print("[3] Show Winners")
        print("[4] Save Progress")
        print("[5] Logout")

        choice = get_valid_choice(1, 5)

        if choice == 1:
            game_main_menu(user)

        elif choice == 2:
            statistics(user_map, user) 
        
        elif choice == 3:
            winners_log(WINNERS_PATH)
            input("\nPress Enter to return to menu...")
        
        elif choice == 4:
            save_user_stats(user_map)
            print("Progress saved.")
            input("\nPress Enter to return to menu...")

        elif choice == 5:
            print("Do you want to logout? [y/n]")
            confirmation = input(">:").strip().lower()
            if confirmation in ("y", "yes", "j", "jo", "jop", "a", "ano"):
                print(f"User {user.username} logged out.")
                return None
        
        else:
            print("Invalid choice, please try again.")


def main():
    # Inicializace and object dict.
    user_map = recreate_user_objects(AUTH_PATH, USERS_DATA_PATH)

    while True:
        # Authentization (Login/Register).
        user = auth_loop(user_map)

        # Not logged user ends the game.
        if not user: 
            print("\nGame ending...")
            break
        
        # Main Menu
        main_menu(user, user_map)

    # Save user statistics.
    save_user_stats(user_map)
    print("Goodbye")


if __name__ == "__main__":
    main()

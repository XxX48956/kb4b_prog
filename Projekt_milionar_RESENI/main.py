from auth import auth_loop
from inicialization import recreate_user_objects
from vars import WINNERS_PATH, AUTH_PATH
from game import game_main_menu
from winners import winners_log


def main_menu(user):
    while True:
        print("Menu")
        print(f"Logged as: {user.username}")
        print("[1] Game")
        print("[2] Stats")
        print("[3] Winners")
        print("[4] Logout")

        try:
            print("Choose option [1-4]:")
            choice = input(">:")
            choice = int(choice)
        except ValueError:
            print("Invalid input. Choose number from 1 to 4.")
            continue

        if choice == 1: # Hlavní hra
            game_main_menu(user)
        elif choice == 2: # Uživatelské statistiky
            pass
        elif choice == 3: # Log výherců Hry
            winners_log(WINNERS_PATH)
        elif choice == 4: # Odhlášení se a zpět do Auth Menu
            print("Do you want to logout? [y/n]")
            confirmation = input(">:").lower()
            if confirmation == "y" or confirmation == "yes":
                print(f"User {user.username} logged out.")
                return None


def main():
    # Vytvoření objektů podle uživatelů v souboru (inicializace)
    recreate_user_objects(AUTH_PATH)
    while True:
        # Atentizace uživatele login/register (vrací objekt uživatele)
        user = auth_loop()

        # Jestli není přihlášen uživatel ukonči program
        if not user: 
            print("Game ending")
            break
        
        # Hlavní menu hry
        main_menu(user)

    print("Goodbye")


if __name__ == "__main__":
    main()

from auth import auth_loop
from inicialization import recreate_user_objects
import vars
from game import game

def winners(WINNERS_PATH):
    with open(WINNERS_PATH, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if not lines:
            print("No winners yet.")
            return None
        cleaned_lines = [line.strip() for line in lines if line.strip("\n")]

        for index, line in enumerate(cleaned_lines, start=1):
            print(f"{index}. {line}")

    return None


def stats():
    pass

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
            game(user)
        elif choice == 2: # Uživatelské statistiky
            stats()
        elif choice == 3: # Log výherců Hry
            winners(vars.WINNERS_PATH)
        elif choice == 4: # Odhlášení se a zpět do Auth Menu
            print("Do you want to logout? [y/n]")
            confirmation = input(">:").lower()
            if confirmation == "y" or confirmation == "yes":
                print(f"User {user.username} logged out.")
                return None


def main():
    # Vytvoření objektů podle uživatelů v souboru (inicializace)
    recreate_user_objects(vars.AUTH_PATH)
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







def game():
    pass



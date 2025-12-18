from registration import register
from login import login   

EXIT_FLAG = "exit"

def get_menu_choice():
    print("\n--- User Authentication Menu ---")    
    while True:
        print("[1] Login")
        print("[2] Register")
        print("[3] Save & Exit")

        try:
            choice = int(input(">:"))
            if 1 <= choice <= 3:
                return choice
            print("Invalid input. \nChoose number 1-3")
        except ValueError:
          print("Invalid input. \nChoose number 1-3")


def confirm_exit():
    print("\nWarning: If you exit now, the program will terminate.")
    confirmation = input("Do you really want to exit? [y/N]: ").strip().lower()
    return confirmation in ("y", "yes")


def authenticate():
    choice = get_menu_choice() # Vizuální menu pro input

    if choice == 1:
        return login() # Vrací objekt/None 
    
    elif choice == 2:
        return register() # Vrací objekt/None
    
    elif choice == 3: # Ukončení programu
        if confirm_exit():
            return EXIT_FLAG
    
    return None


def auth_loop(): # Dokud není uživatel nebo 'exit' opakuj autentizaci  
    while True:
        user = authenticate()
        if user == EXIT_FLAG:
            return None
        
        if user: 
            return user

    return None
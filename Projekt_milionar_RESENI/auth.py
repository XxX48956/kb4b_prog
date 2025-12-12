from registration import register
from login import login   


def auth_menu():
    print("User Authentication Menu")
    
    while 1:
        print("[1] Login")
        print("[2] Register")
        print("[3] Exit")

        try:
            choice = int(input(">:"))
            return choice
        except:
          print("Invalid input. \nChoose number 1-3")


def auth():
    choice = auth_menu() # Vizuální menu pro input

    if choice == 1:
        return login() # Vrací objekt/None 
    
    elif choice == 2:
        return register() # Vrací objekt/None
    
    elif choice == 3: # Ukončení programu
        print("If you exit without authentization program will end.")
        confirmation = input("Do you want to exit? [y/n] \n>:").lower()

        if confirmation == "y" or confirmation == "yes":
            return "exit"
        else: 
            return None
    else:
        print("Invalid choice. \nChoose in range 1-3")
    
    return None


def auth_loop(): # Dokud není uživatel nebo 'exit' opakuj autentizaci  
    while True:
        user = auth()
        if user == "exit":
            return
        
        if user: 
            return user

    return None
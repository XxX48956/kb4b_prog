from registration import register
from login import login   
import vars


def authMenu():
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
    choice = authMenu()

    if choice == 1:
        return login()
    elif choice == 2:
        return register()
    elif choice == 3:
        vars.end()
        return None
    else:
        print("Invalid choice. \nChoose in range 1-3")
    
    return None
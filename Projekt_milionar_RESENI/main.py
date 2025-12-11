from auth import auth
from inicialization import recreate_user_objects
import vars


def auth_loop():    
    while not vars.EXIT:
        user = auth()
        if user: 
            return user

    return None

def main():
    #vytvoření objektů podle uživatelů v souboru
    recreate_user_objects(vars.AUTH_PATH)

    user = auth_loop()

    while not vars.EXIT:
        print("Program běží...")
    
    print("Goodbye!")



if __name__ == "__main__":
    main()
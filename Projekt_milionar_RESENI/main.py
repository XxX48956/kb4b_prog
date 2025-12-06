from milionar import auth
import vars



def auth_loop():

    while not vars.EXIT:
        user = auth()
        if user: 
            return user

    return None

def main():

    user = auth_loop()

    while not vars.EXIT:
        print("Program běží...")



if __name__ == "__main__":
    main()
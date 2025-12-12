from auth import auth_loop
from inicialization import recreate_user_objects
import vars


def main():
    # Vytvoření objektů podle uživatelů v souboru (inicializace)
    recreate_user_objects(vars.AUTH_PATH)

    # Atentizace uživatele login/register (vrací objekt uživatele)
    user = auth_loop()
    # Jestli není přihlášen uživatel ukonči program
    if not user: return

    # Hlavní loop hry   *Dodělat Logout/Exit
    while True: # (not vars.EXIT)
        print("Program běží...")

    print("Goodbye")
    return none


if __name__ == "__main__":
    main()
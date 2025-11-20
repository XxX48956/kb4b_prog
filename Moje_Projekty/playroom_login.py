
class Account:
    def __init__(self):
        self.name = self.register_name()
        self.password = self.register_password()
        self.balance = 1000

    def register_name(self):
        return input("Zadej uživ. jméno: ")
    def register_password(self):
        return input("Zadej heslo: ")
def menu():
    accounts = []

    while 1:
        print("[1]Register \n[2]Login \n[3]Exit")
        choice = int(input())
        if choice == 1:
            accounts.append(Account())
            print("Success")
        elif choice == 2:
            pass
        elif choice == 3:
            print("Nashledanou")
            break
        else:
            print("Špatná hodnota")

menu()
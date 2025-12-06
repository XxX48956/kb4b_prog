class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __del__(self): #Dodělat zápis dat z objektu do souboru
        print(f"Objekt se jménem {self.username} byl smazán")
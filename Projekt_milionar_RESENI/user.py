class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.games = 0 # Počet začatých her
        self.wins = 0 # Počet výher

    

    def __del__(self): #Dodělat zápis dat z objektu do souboru
        print(f"Objekt se jménem {self.username} byl smazán")
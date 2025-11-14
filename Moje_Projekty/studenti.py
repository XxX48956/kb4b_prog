import random



def vyber_random_studenta(text):
    return random.choice(text).strip("\n")

def vyber_studentu(n, path):
    vybrani_studenti = []

    with open(path, "r", encoding="utf-8") as file:
        text = file.readlines()
        if len(text) < n:
            print("Nedostatek studentů")
            return
        
        for _ in range(n):
            choosen = vyber_random_studenta(text)
            if choosen not in vybrani_studenti:
                vybrani_studenti.append(choosen)
            else:
                vyber_random_studenta(text)

        for each in sorted(vybrani_studenti):
            print(each)
vyber_studentu(22, "2. prace_se_soubory\data\studenti.txt")
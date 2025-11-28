import csv


path = r"2. prace_se_soubory\data\vira_v_cesku.csv"

def fav_vira(path):
        
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        neviry = ["Bez náboženské víry", "Neuvedeno", "věřící - nehlásící se k žádné církvi ani náboženské společnosti"]
        max_hodnota = 0
        vira = ""
        for line in reader:
            if line["uzemi_txt"] == "Brno" and line["vira_txt"] != "" and line["vira_txt"] not in neviry:

                if int(line["hodnota"]) > max_hodnota:
                    max_hodnota = int(line["hodnota"])
                    vira = line["vira_txt"]

        print(max_hodnota, vira)


def pocet_nabozenstvi_a_vericich(path):
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        pocet_nabozenstvi = []
        pocet_vericich = 0
        prumer_vericich = {}
        arr = []

        for line in reader:
            if line["uzemi_txt"] == "Brno":
               pocet_vericich += int(line["hodnota"])
               arr.append(line["vira_txt"]) 
        for i in set(arr):
            print(len(set(arr)))

        print(pocet_vericich)


pocet_nabozenstvi_a_vericich(path)



def x():
    import pandas as pd
    import matplotlib.pyplot as plt

    # Načtení datasetu
    df = pd.read_csv(r'2. prace_se_soubory\data\vira_v_cesku.csv')

    # Filtrování dat pro Brno
    brno_data = df[df['uzemi_txt'] == 'Brno']

    # Nejpopulárnější víra v Brně
    popular_religion = brno_data.loc[brno_data['hodnota'].idxmax()]

    print(f"Nejpoužívanější víra v Brně: {popular_religion['vira_txt']} s {popular_religion['hodnota']} věřícími.")

    # Kolik máme různých náboženství a věřících v Brně
    total_religions_brno = brno_data['vira_txt'].nunique()
    total_believers_brno = brno_data['hodnota'].sum()
    average_believers_per_religion = total_believers_brno / total_religions_brno

    print(f"Celkový počet různých náboženství v Brně: {total_religions_brno}")
    print(f"Celkový počet věřících v Brně: {total_believers_brno}")
    print(f"Průměrný počet věřících na jedno náboženství v Brně: {average_believers_per_religion:.2f}")

    # Kolik lidí má jako víru "Jedi"
    jedi_data = df[df['vira_txt'].str.contains('Jedi', case=False)]
    jedi_count = jedi_data['hodnota'].sum()
    jedi_city = jedi_data.loc[jedi_data['hodnota'].idxmax(), 'uzemi_txt']

    print(f"Počet lidí, kteří mají jako víru 'Jedi': {jedi_count} v městě {jedi_city}.")

    # Vytvoření koláčového grafu
    no_religion = df[df['vira_txt'] == 'Bez náboženské víry']['hodnota'].sum()
    total_believers = df['hodnota'].sum()

    labels = ['Bez náboženské víry', 'Celkový součet věřících']
    sizes = [no_religion, total_believers]

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Podíl bez náboženské víry a celkový součet věřících')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

    # Uživatel zadá víru
    user_religion = input("Zadejte víru, kterou chcete prověřit: ")

    if user_religion in df['vira_txt'].values:
        user_data = df[df['vira_txt'] == user_religion]
        total_user_believers = user_data['hodnota'].sum()
        top_areas = user_data.nlargest(3, 'hodnota')[['uzemi_txt', 'hodnota']]
        
        print(f"Celkový počet věřících pro '{user_religion}': {total_user_believers}")
        print(f"3 území s největším počtem věřících pro '{user_religion}':")
        print(top_areas)
    else:
        print(f"Víra '{user_religion}' nebyla nalezena.")

import csv
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# ---------- Načtení CSV a úprava dat ----------
X = []  # Vstupy: Open, High, Low, Volume
Y = []  # Výstup: Close cena

# Předpokládáme soubor 'tesla_stock.csv' ve složce 'data'
with open("3. strojove_uceni/data/TSLA_Stock.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Převedeme textové hodnoty na čísla
        open_p = float(row["Open"])
        high_p = float(row["High"])
        low_p = float(row["Low"])
        volume = float(row["Volume"])
        close_p = float(row["Close"])

        # Do X dáváme parametry, které známe dopředu (před uzavřením trhu)
        X.append([open_p, high_p, low_p, volume])
        Y.append(close_p)

# ---------- Rozdělení na trénování a testování ----------
# train_test_split udělá práci za nás (80% trénink, 20% test)
trening_X, test_X, trening_Y, test_Y = train_test_split(
    X, Y, 
    test_size=0.2, 
    random_state=42
)

# ---------- Neuronová síť (Regrese) ----------
# Používáme MLPRegressor pro předpověď spojité hodnoty (ceny)
neural_network = MLPRegressor(
    # 1. Zvýšení kapacity: Tři vrstvy umožňují zachytit komplexnější vzorce
    hidden_layer_sizes=(64, 32, 16), 
    
    # 2. Aktivace: 'tanh' nebo 'relu' jsou fajn, ale 'relu' je u hlubších sítí stabilnější
    activation="relu", 
    
    # 3. Solver: Pro středně velké datasety je Adam skvělý. 
    # Pokud máš málo dat (pod 1000 řádků), zkus 'lbfgs'.
    solver="adam",
    
    # 4. Učení: Menší learning_rate zajistí, že model "nepřestřelí" optimum
    learning_rate_init=0.001,
    
    # 5. Regularizace (Alpha): Klíčové pro akcie! 
    # Vyšší hodnota (např. 0.01) brání overfittingu na náhodný šum.
    alpha=0.01,
    
    # 6. Automatické zastavení: Zabrání zbytečnému trénování, když se přesnost nezlepšuje
    early_stopping=True,
    validation_fraction=0.1,
    n_iter_no_change=20,
    
    max_iter=10000, 
    random_state=4
)

print("Trénuji model...")
neural_network.fit(trening_X, trening_Y)

# ---------- Vyhodnocení ----------
predikce = neural_network.predict(test_X)

# U regrese měříme průměrnou chybu (o kolik se model v průměru mýlí)
chyba = mean_absolute_error(test_Y, predikce)
print(f"Průměrná chyba predikce: {chyba:.2f} USD")

# ---------- Vizualizace výsledků ----------
# Zobrazíme první 50 hodnot pro porovnání reality vs. predikce
plt.figure(figsize=(10, 5))
plt.plot(test_Y[:50], label="Skutečná cena", color="blue", marker='o')
plt.plot(predikce[:50], label="Predikce sítě", color="red", linestyle='--', marker='x')
plt.title("Porovnání skutečné Close ceny a predikce")
plt.xlabel("Vzorek (dny)")
plt.ylabel("Cena v USD")
plt.legend()
plt.grid(True)
plt.show()
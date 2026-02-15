import csv

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

from sklearn.preprocessing import StandardScaler

# ---------- Načtení CSV a úprava dat ----------
X = []  # = vstupy
Y = []  # = výstupy
path = "Moje neuronka/winequality-red.csv"



with open(path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        if int(row["quality"]) in (3, 4, 8):
            continue
        fixed_acidity = float(row["fixed acidity"])
        volatile_acidity = float(row["volatile acidity"])
        citric_acid = float(row["citric acid"])
        residual_sugar = float(row["residual sugar"])
        chlorides = float(row["chlorides"])
        free_sulfur_dioxide = float(row["free sulfur dioxide"])
        total_sulfur_dioxide = float(row["total sulfur dioxide"])
        density = float(row["density"])
        pH = float(row["pH"])
        sulphates = float(row["sulphates"])
        alcohol = float(row["alcohol"])

        quality = int(row["quality"])
        
        Y.append(quality)
        X.append([fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol])
        


# ---------- Rozdělení na trénování a testování ----------
trening_X, test_X, trening_Y, test_Y = train_test_split(
    X, Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)
scaler = StandardScaler()

trening_X = scaler.fit_transform(trening_X)
test_X = scaler.transform(test_X)

neural_network = MLPClassifier(
    hidden_layer_sizes=(128, 85, 134),
    activation='relu',
    solver='adam',
    alpha=0.0001,
    learning_rate_init=0.001,
    max_iter=2000,
    early_stopping=True,
    n_iter_no_change=20,
    random_state=42
)




neural_network.fit(trening_X, trening_Y)

# ---------- Vyhodnocení ----------
results = neural_network.predict(test_X)

correct = 0
for i in range(len(results)):
    if test_Y[i] == results[i]:
        correct += 1
print("Přesnost:", correct / len(results))

# ---------- Confusion matrix ----------
# zobrazuje jaké odpovědi dává neuronka pro dané vstupy
ConfusionMatrixDisplay.from_predictions(
    test_Y, results)
plt.show()


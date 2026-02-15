import csv
import pandas as pd # Doporučuji pro snazší práci s daty
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import ConfusionMatrixDisplay, classification_report
import matplotlib.pyplot as plt

# 1. Načtení dat pomocí pandas (mnohem čistší než csv reader)
path = "Moje neuronka\winequality-red.csv"
data = pd.read_csv(path, sep=";")

# Odstranění méně zastoupených tříd (volitelné, ale pomáhá stabilitě)
# data = data[~data['quality'].isin([3, 4, 8])]

X = data.drop('quality', axis=1)
y = data['quality']

# 2. Rozdělení dat
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. ŠKÁLOVÁNÍ - zásadní pro MLP
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Optimalizovaná neuronová síť
neural_network = MLPClassifier(
    hidden_layer_sizes=(128, 64), # Žádná úzká hrdla
    activation='relu',            # Modernější než tanh
    solver='adam',
    alpha=0.001,                  # Regularizace proti overfittingu
    max_iter=2000,                # Více prostoru pro učení
    early_stopping=True,          # Zastaví se, když se přestane zlepšovat
    validation_fraction=0.1,
    random_state=42
)

neural_network.fit(X_train_scaled, y_train)

# 5. Vyhodnocení
score = neural_network.score(X_test_scaled, y_test)
print(f"Přesnost na testovacích datech: {score:.4f}")

# Detailní report
predictions = neural_network.predict(X_test_scaled)
print(classification_report(y_test, predictions))

# Confusion Matrix

ConfusionMatrixDisplay.from_predictions(y_test, predictions)
plt.title("Matice záměn (Wine Quality)")
plt.show()
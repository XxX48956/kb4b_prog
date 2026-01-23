import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 1. Načtení dat pomocí pandas (mnohem rychlejší a čistší)
df = pd.read_csv("3. strojove_uceni/data/TSLA_Stock.csv")

# Definice vstupů a výstupu
X = df[["Open", "High", "Low", "Volume"]]
y = df["Close"]

# 2. Rozdělení na trénovací a testovací sadu
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. ŠKÁLOVÁNÍ DAT (Zásadní pro neuronové sítě)
# Transformuje data tak, aby měla průměr 0 a odchylku 1
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Konfigurace a trénink modelu
model = MLPRegressor(
    hidden_layer_sizes=(128, 64, 32, 16, 8), # Dvě vrstvy bohatě stačí
    activation="relu",
    solver="adam",
    #alpha=0.001,               # Jemná regularizace
    max_iter=2000,             # Více než dost pro konvergenci
    #early_stopping=True,       # Zastaví, pokud se model přestane zlepšovat
    random_state=42
)

print("Trénuji model...")
model.fit(X_train_scaled, y_train)

# 5. Predikce a vyhodnocení
preds = model.predict(X_test_scaled)
mae = mean_absolute_error(y_test, preds)
rmse = np.sqrt(mean_squared_error(y_test, preds))
print(f"Průměrná chyba (MAE): {mae:.2f} USD")
print(f"Odmocnina průměrné čtvercové chyby (RMSE): {rmse:.2f} USD")

# 6. Vizualizace
plt.figure(figsize=(12, 6))
plt.plot(y_test.values[:50], label="Realita", color="#1f77b4", linewidth=2)
plt.plot(preds[:50], label="Predikce", color="#ff7f0e", linestyle="--")
plt.title("Předpověď ceny akcií TSLA (MLP Regressor)")
plt.ylabel("Cena (USD)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
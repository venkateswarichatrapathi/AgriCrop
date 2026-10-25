import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

np.random.seed(42)

# Typical (approximate) soil ranges for each crop: (N, P, K, pH)
# Each entry: (N_min, N_max, P_min, P_max, K_min, K_max, pH_min, pH_max)
crop_ranges = {
    "Rice":      (60, 100, 35, 60,  35, 45,  5.0, 6.5),
    "Wheat":     (80, 120, 40, 60,  30, 50,  6.0, 7.5),
    "Maize":     (70, 110, 40, 70,  15, 30,  5.5, 7.0),
    "Cotton":    (100, 140, 35, 60, 15, 25,  6.0, 8.0),
    "Groundnut": (10, 40,  50, 80,  20, 45,  6.0, 7.0),
}

# Generate 100 samples per crop
rows = []
for crop, (n_lo, n_hi, p_lo, p_hi, k_lo, k_hi, ph_lo, ph_hi) in crop_ranges.items():
    for _ in range(100):
        rows.append({
            "N": np.random.randint(n_lo, n_hi + 1),
            "P": np.random.randint(p_lo, p_hi + 1),
            "K": np.random.randint(k_lo, k_hi + 1),
            "pH": round(np.random.uniform(ph_lo, ph_hi), 2),
            "Crop": crop,
        })

df = pd.DataFrame(rows)
df.to_csv("crop_data.csv", index=False)
print("Dataset created:", df.shape)

# Split features and target
X = df[["N", "P", "K", "pH"]]
y = df["Crop"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"Model accuracy: {accuracy * 100:.2f}%")

# Save model
joblib.dump(model, "crop_model.pkl")
print("Model saved as crop_model.pkl")
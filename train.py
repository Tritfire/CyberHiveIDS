import argparse
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from joblib import dump
import os

parser = argparse.ArgumentParser()
parser.add_argument("--input_data", type=str)
parser.add_argument("--output_model", type=str)
args = parser.parse_args()

# Charger les données prétraitées
df = pd.read_csv(args.input_data)

# Séparer les features et le label
X = df.drop(columns=["label"], errors="ignore")
y = df["label"] if "label" in df.columns else None

# Créer le dossier de sortie si inexistant
os.makedirs(args.output_model, exist_ok=True)

# Entraînement du modèle supervisé (Random Forest)
if y is not None:
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X, y)
    dump(rf_model, os.path.join(args.output_model, "rf_model.joblib"))
    print("✅ RandomForest entraîné et sauvegardé")

# Entraînement du modèle non supervisé (Isolation Forest)
iso_forest = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
iso_forest.fit(X)
dump(iso_forest, os.path.join(args.output_model, "iso_forest.joblib"))
print("✅ IsolationForest entraîné et sauvegardé")

print(f"✅ Modèles IDS sauvegardés dans {args.output_model}")
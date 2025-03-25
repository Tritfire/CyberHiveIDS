import argparse
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from joblib import dump

# 📌 Définir les arguments
parser = argparse.ArgumentParser()
parser.add_argument("--input_data", type=str, required=True, help="Chemin vers le dossier contenant preprocessed.csv")
parser.add_argument("--output_model", type=str, required=True, help="Dossier de sortie pour les modèles")
args = parser.parse_args()

# 📥 Charger les données prétraitées
input_path = os.path.join(args.input_data, "preprocessed.csv")
df = pd.read_csv(input_path)

# ✅ Séparer X et y
X = df.drop(columns=["label"], errors="ignore")
y = df["label"]

# ✅ Créer le dossier de sortie
os.makedirs(args.output_model, exist_ok=True)

# ✅ Sauvegarder les noms des colonnes utilisées
with open(os.path.join(args.output_model, "feature_names.txt"), "w") as f:
    f.write(",".join(X.columns))

# ✅ Entraîner RandomForest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X, y)
dump(rf_model, os.path.join(args.output_model, "rf_model.joblib"))
print("✅ RandomForest entraîné et sauvegardé.")

# ✅ Entraîner IsolationForest
iso_forest = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
iso_forest.fit(X)
dump(iso_forest, os.path.join(args.output_model, "iso_forest.joblib"))
print("✅ IsolationForest entraîné et sauvegardé.")

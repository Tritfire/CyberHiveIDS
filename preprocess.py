import argparse
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os

# 📌 1. Définition des arguments pour Azure ML
parser = argparse.ArgumentParser()
parser.add_argument("--input_data", type=str, required=True, help="Chemin vers le fichier d'entrée")
parser.add_argument("--output_data", type=str, required=True, help="Chemin vers le fichier de sortie")
args = parser.parse_args()

# 📌 2. Charger les données IDS
print(f"📥 Chargement des données depuis : {args.input_data}")
df = pd.read_csv(args.input_data)

# 📌 3. Suppression des colonnes inutiles (si elles existent)
columns_to_drop = ["id", "timestamp"]
df = df.drop(columns=[col for col in columns_to_drop if col in df.columns], errors="ignore")

# 📌 4. Encodage des labels si la colonne "label" existe
if "label" in df.columns:
    print("🔄 Encodage de la colonne 'label'...")
    label_encoder = LabelEncoder()
    df["label"] = label_encoder.fit_transform(df["label"])

# 📌 5. Normalisation des features numériques
print("📊 Normalisation des données...")
scaler = StandardScaler()
df.iloc[:, :-1] = scaler.fit_transform(df.iloc[:, :-1])

# 📌 6. Création du dossier de sortie (si inexistant)
os.makedirs(os.path.dirname(args.output_data), exist_ok=True)

# 📌 7. Sauvegarde des données prétraitées
df.to_csv(args.output_data, index=False)
print(f"✅ Données prétraitées sauvegardées dans : {args.output_data}")

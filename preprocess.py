import argparse
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Arguments d'entrée
parser = argparse.ArgumentParser()
parser.add_argument("--raw_data", type=str, help="Chemin vers les données brutes")
parser.add_argument("--preprocessed_data", type=str, help="Répertoire de sortie")
args = parser.parse_args()

# 📥 Charger les données brutes
df = pd.read_csv(args.raw_data)

# Nettoyage : supprimer colonnes non exploitables
cols_to_drop = [
    "timestamp", "src_ip", "dest_ip",
    "payload_md5", "payload_sha512",
    "alert_signature", "category", "attack"  # attack sera transformée
]
df_cleaned = df.drop(columns=cols_to_drop, errors="ignore")

# Encoder 'protocol' si présente
if "protocol" in df_cleaned.columns:
    le = LabelEncoder()
    df_cleaned["protocol"] = le.fit_transform(df_cleaned["protocol"])

# Ajouter la colonne 'label' à partir de 'attack'
df["label"] = df["attack"].astype(bool).astype(int)
df_cleaned["label"] = df["label"]

# Créer le dossier de sortie si nécessaire
os.makedirs(args.preprocessed_data, exist_ok=True)

# Sauvegarder les données nettoyées
output_path = os.path.join(args.preprocessed_data, "preprocessed.csv")
df_cleaned.to_csv(output_path, index=False)
print(f"Données prétraitées sauvegardées à {output_path}")

import argparse
import pandas as pd

# 📌 1. Définition des arguments pour Azure ML
parser = argparse.ArgumentParser()
parser.add_argument("--input_data", type=str, required=True, help="Chemin vers le fichier d'entrée")
parser.add_argument("--output_data", type=str, required=True, help="Chemin vers le fichier de sortie")
args = parser.parse_args()

# 📌 2. Charger les données IDS sans modification
print(f"📥 Chargement des données depuis : {args.input_data}")
df = pd.read_csv(args.input_data)

# 📌 3. Ignorer le prétraitement (bypass)
print("⚠️ Prétraitement désactivé - les données restent inchangées.")

# 📌 4. Sauvegarde des données inchangées
df.to_csv(args.output_data, index=False)
print(f"✅ Données sauvegardées sans modification : {args.output_data}")
import pandas as pd
import requests
import json

# Chargement du dataset brut
df = pd.read_csv("test_data.csv")

# Suppression des colonnes non utilisées à l'entraînement
colonnes_a_supprimer = ["timestamp", "attack"]  # On ajoute "attack"
df = df.drop(columns=colonnes_a_supprimer, errors="ignore")

# Conversion en JSON
payload = json.loads(df.to_json(orient="records"))

# Configuration du scoring
endpoint = "https://cyberhiveids-endpoint.eastus.inference.ml.azure.com/score"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 2na1El4XxdbmJvy2UVY7N7f5rHlVBlhtdFL7Mj5wMygE1lI5qMzpJQQJ99BDAAAAAAAAAAAAINFRAZML1DbQ"
}

# Envoi de la requête
response = requests.post(endpoint, headers=headers, json=payload)

# Résultats
print(f"Status Code: {response.status_code}")
result = response.json()
print("Scoring Results:", result)

a = 0
b = 0
# Enregistrement des résultats si tout s'est bien passé
if response.status_code == 200 and "predictions" in result:
    df["prediction"] = result["predictions"]
    df.to_csv("results_with_predictions.csv", index=False)
    print("✅ Résultats enregistrés dans results_with_predictions.csv")
    for i in result["predictions"]:
        if (i):
            a += 1
        b += 1
    c = (a*100)/b
    print(c)
elif "error" in result:
    print("❌ Erreur côté serveur Azure :", result["error"])
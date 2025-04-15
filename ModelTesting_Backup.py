import pandas as pd
import requests
import json
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Chargement du dataset
df = pd.read_csv("test_data.csv")

# Encodage des colonnes catégorielles
label_encoders = {}
for col in ['protocol', 'src_ip', 'dst_ip', 'message']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Features et target
X = df.drop(columns=['attack', 'timestamp'])
y = df['attack'].astype(int)

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Préparation du payload
payload = json.loads(df.to_json(orient="records"))

# Infos d'accès
endpoint = "https://cyberhiveids-endpoint.eastus.inference.ml.azure.com/score"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer 2na1El4XxdbmJvy2UVY7N7f5rHlVBlhtdFL7Mj5wMygE1lI5qMzpJQQJ99BDAAAAAAAAAAAAINFRAZML1DbQ"
}

# Envoi
response = requests.post(endpoint, headers=headers, json=payload)

# Résultat
print(f"Status Code: {response.status_code}")
print("Scoring Results:", response.json())

# Enregistrement des résultats
if response.status_code == 200 and "predictions" in response.json():
    df["prediction"] = response.json()["predictions"]
    df.to_csv("results_with_predictions.csv", index=False)

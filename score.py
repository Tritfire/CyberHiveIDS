import joblib
import pandas as pd
import json
import os
import numpy as np

def init():
    global model, encoders
    model_bundle_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "random_forest_and_encoders.joblib")
    model_bundle = joblib.load(model_bundle_path)

    model = model_bundle["model"]
    encoders = model_bundle["encoders"]

def run(raw_data):
    try:
        df = pd.read_json(raw_data, orient='records')

        # Appliquer les encoders avec gestion des valeurs inconnues
        for col in encoders:
            if col in df.columns:
                encoder = encoders[col]
                known_classes = set(encoder.classes_)

                # Remplace les valeurs inconnues par None
                df[col] = df[col].apply(lambda x: x if x in known_classes else None)

                # Si None pas déjà dans encoder, on l’ajoute pour éviter l’erreur
                if None not in encoder.classes_:
                    encoder.classes_ = np.append(encoder.classes_, None)

                # Transforme avec -1 pour None
                df[col] = df[col].map(lambda x: -1 if x is None else encoder.transform([x])[0])

        # Prédictions
        predictions = model.predict(df)
        return {"predictions": predictions.tolist()}

    except Exception as e:
        return {"error": str(e)}

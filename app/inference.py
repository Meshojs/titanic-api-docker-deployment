import torch
import pandas as pd
import numpy as np
import joblib
from app.model import Model

# Load artifacts once at import time
scaler = joblib.load("artifacts/scaler.pkl")
feature_columns = joblib.load("artifacts/feature_columns.pkl")

model = Model(infeatures=len(feature_columns))
model.load_state_dict(torch.load("artifacts/Model.pth", map_location="cpu"))
model.eval()


def predict(passenger: dict) -> dict:
    """
    Takes a raw passenger dict (matching PassengerInput schema),
    applies the exact same preprocessing as training, and returns a prediction.
    """
    df = pd.DataFrame([passenger])

    # Same preprocessing as training
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    df = pd.get_dummies(df, columns=["Pclass"], drop_first=False, dtype=int)

    # Align columns exactly to training (adds missing one-hot cols as 0, drops extras, fixes order)
    df = df.reindex(columns=feature_columns, fill_value=0)

    # Scale using the SAME fitted scaler
    x_scaled = scaler.transform(np.array(df))
    x_tensor = torch.tensor(x_scaled, dtype=torch.float32)

    with torch.no_grad():
        logits = model(x_tensor)
        probability = torch.sigmoid(logits).item()
        survived = probability >= 0.5

    return {
        "survived": survived,
        "survival_probability": round(probability, 4)
    }
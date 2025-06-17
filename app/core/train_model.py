import sys
from pathlib import Path

# Project root to python Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump
from app.core.config import MODEL_FILE, DATA_FILE
from schemas.data_schemas import ACDataPoint
import numpy as np

def load_and_preprocess_data():
    # Loads data and converts it to ML-ready format
    df = pd.read_csv(DATA_FILE)

    # Validate Schema
    try:
        ACDataPoint(**df.iloc[0].to_dict())
    except Exception as e:
        raise ValueError(f"Data validation failed: {e}")
    
    # Convert categorical features
    df = pd.get_dummies(df, columns=['season', 'weather'])

    # Separate features (X) and target (y)
    X = df.drop('ac_state', axis=1)
    y = df['ac_state'].map({"On": 1, "Off": 0})

    return X, y

def train_and_evaluate():
    # Trains model and evaluate performance
    X, y = load_and_preprocess_data()

    # Split data (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Initialize and train model
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42
    )
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    print("\n--- Model Performance ---")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}")
    print(classification_report(y_test, y_pred))

    # Save model
    Path(MODEL_FILE).parent.mkdir(exist_ok=True)
    dump(model, MODEL_FILE)
    print(f"\n Model saved to {MODEL_FILE}")

if __name__ == "__main__":
    train_and_evaluate()
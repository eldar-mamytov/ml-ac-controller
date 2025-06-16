# Founation utilities for data handling and weather simulatiuon.

import pandas as pd
from pathlib import Path
from config import DATA_FILE

def load_data() -> pd.DataFrame:
    # Load dataset from CSV with validation chekcs
    if not Path(DATA_FILE).exists():
        raise FileNotFoundError(f"Data file not found at {DATA_FILE}")
    return pd.read.csv(DATA_FILE)

def save_data(df: pd.DataFrame) -> None:
    # Save dataset to CSV with directory creation
    Path(DATA_FILE).parent.mkdir(exist_ok=True)
    df.to_csv(DATA_FILE, index=False)


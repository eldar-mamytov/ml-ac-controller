import joblib
import numpy as np
import pandas as pd
from schemas.data_schemas import ACDataPoint
from config import MODEL_FILE
from typing import Dict, Literal

PredictionResult = Dict[Literal["ac_state", "confidence"],str]

class ACPredictor:
    def __init__(self):
        self.model = joblib.load(MODEL_FILE)
        self.feature_order = self.model.feature_names_in_

    # Converts user input to model-compatible format
    def preprocess_input(self, features: dict) -> pd.DataFrame:
        
        validated = ACDataPoint(**features).model_dump()

        # Create DataFrame with all possible columns
        df = pd.DataFrame([validated])
        df = pd.get_dummies(df)

        for col in self.feature_order:
            if col not in df.columns:
                df[col] = 0

        return df[self.feature_order]
    
    # Makes prediction with confidence score
    def predict(self, features: dict) -> PredictionResult:
        X = self.preprocess_input(features)
        proba = self.model.predict_proba(X)[0]
        prediction = self.model.predict(X)[0]

        return {
            "ac_state": "On" if prediction == 1 else "Off",
            "confidence": f"{max(proba)*100:.1f}%"
        }
    
    @staticmethod
    def get_user_input() -> dict:
        print("\n--- AC State Predictor ---")
                
        while True:
            try:
                temperature = float(input("Current temperature (°F): "))
                break
            except ValueError:
                print("❌ Invalid temperature. Please enter a number.")
        
        while True:
            try:
                humidity = float(input("Humidity (%): "))
                break
            except ValueError:
                print("❌ Invalid humidity. Please enter a number.")
        
        valid_seasons = ["winter", "spring", "summer", "autumn"]
        while True:
            season = input("Season (winter/spring/summer/autumn): ").strip().lower()
            if season in valid_seasons:
                break
            else:
                print(f"❌ Invalid season. Please choose from: {', '.join(valid_seasons)}")
        
        while True:
            try:
                occupancy = int(input("Number of people in room: "))
                break
            except ValueError:
                print("❌ Invalid number. Please enter an integer.")
        
        valid_weather = ["sunny", "cloudy", "rainy", "snow"]
        while True:
            weather = input("Weather (sunny/cloudy/rainy/snow): ").strip().lower()
            if weather in valid_weather:
                break
            else:
                print(f"❌ Invalid weather. Please choose from: {', '.join(valid_weather)}")
        
        return {
            "temperature": temperature,
            "humidity": humidity,
            "season": season,
            "occupancy": occupancy,
            "weather": weather
        }
        
    
if __name__ == "__main__":
    predictor = ACPredictor()
    while True:
        try:
            features = ACPredictor.get_user_input()
            result = predictor.predict(features)
            print(f"\nPrediction: AC should be {result['ac_state']} (confidence: {result['confidence']})")
        except ValueError as e:
            print(f"Invalid input: {e}")
        except KeyboardInterrupt:
            print("\nBye!")
        break
import numpy as np
import pandas as pd
from utils.weather_simulation import generate_weather
from schemas.data_schemas import ACDataPoint, Season
from config import DATA_FILE
from pathlib import Path

def generate_case() -> dict:
    # Generates one validated data point
    season: Season = np.random.choice(list(Season.__args__))
    temp, weather = generate_weather(season)

    # Smart AC Logic (prioritizes your patterns)
    if season == "summer":
        if temp > 78 or (weather == "sunny" and temp > 75):
            ac_state = "On"
        else:
            ac_state = "Off"
    elif season == "winter":
        if temp < 68 or weather in ["snow", "rain"]:
            ac_state = "On"
        else:
            ac_state = "Off"
    elif season == "spring":
        if temp > 72 and weather == "sunny":
            ac_state = "On"
        elif temp < 65 and weather in ["rain", "cloudy"]:
            ac_state = "On"
        else:
            ac_state = "Off"
    elif season == "autumn":
        if temp < 67 and weather in ["rain", "cloudy"]:
            ac_state = "On"
        elif temp > 75 and weather == "sunny":
            ac_state = "On"
        else:
            ac_state = "Off"
    else:
        ac_state = "Off"


    return ACDataPoint(
        temperature=temp,
        humidity=np.random.randint(30,80),
        season=season,
        occupancy=np.random.randint(0,5),
        weather=weather,
        ac_state=ac_state
    ).model_dump() 

def generate_dataset(n_samples=500):
    # Generates and saves synthetic data
    data = [generate_case() for _ in range(n_samples)]
    Path(DATA_FILE).parent.mkdir(exist_ok=True)
    pd.DataFrame(data).to_csv(DATA_FILE, index=False)
    print(f"Generated {len(data)} samples at {DATA_FILE}")


if __name__ == "__main__":
    generate_dataset()

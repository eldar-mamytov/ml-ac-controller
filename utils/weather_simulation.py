import numpy as np
from app.core.config import SEASON_TEMPS, WEATHER_PROBS
from schemas.data_schemas import Weather

def generate_weather(season: str) -> tuple:
    # Generate realistic weather data for a given season
    if season not in SEASON_TEMPS:
        raise ValueError(f"Invalid season; {season}")
    
    # Generate temperature
    temp_range = SEASON_TEMPS[season]
    outside_temp = np.random.uniform(*temp_range)

    #Generate weather condition
    weather_options = list(WEATHER_PROBS[season].keys())
    weather_probs = list(WEATHER_PROBS[season].values())
    weather: Weather = np.random.choice(weather_options, p=weather_probs)


    return round(outside_temp, 1), weather
from pydantic import BaseModel, validator, Field, ValidationError
from typing import Literal, Annotated
from config import SEASON_TEMPS

# Define allowed values
Season = Literal["winter", "spring", "summer", "autumn"]
ACState = Literal["On", "Off"]
Weather = Literal["sunny", "cloudy", "rainy", "snow"]

class ACDataPoint(BaseModel):
    temperature: Annotated[float, Field(ge=-20, le=120)]   # Fahrenheit range
    humidity: Annotated[float, Field(ge=0, le=100)]        # Percentage\
    season: Season
    occupancy: Annotated[int, Field(ge=0, le=10)]          # 0-10 peple
    weather: Weather
    ac_state: ACState

    @validator('temperature')
    def check_season_temp(cls, v, values):
        season = values.get('season')
        if season and (v < SEASON_TEMPS[season][0] or v > SEASON_TEMPS[season][1]):
            raise ValueError(f"Temperature {v}°F is unrealistic for {season}")
        return v
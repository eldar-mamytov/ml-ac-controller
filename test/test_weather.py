import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import weather_simulation

temp, weather = weather_simulation.generate_weather("spring")
print(f"Summer weather: {temp}F, {weather}")
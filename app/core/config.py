'''
The project configuration file. This will store all our constants and settings in one place.

File Purpose
Stores global variables (e.g., temperature unit, file paths)
Makes it easy to change settings without digging through code
'''
    
# Project Configuration
import os

# Temperature Unit (Fahrenheit)
USE_FAHRENHEIT = True

# File Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
MODELS_DIR = os.path.join(BASE_DIR, 'models')
SCHEMAS_DIR = os.path.join(BASE_DIR, 'schemas')
UTILS_DIR = os.path.join(BASE_DIR, 'utils')

# Data Files
DATA_FILE = os.path.join(DATA_DIR, 'ac_data.csv')
MODEL_FILE = os.path.join(MODELS_DIR, 'ac_model.joblib')

# Schema Files
SCHEMA_FILE = os.path.join(SCHEMAS_DIR, 'data_schemas.py')

# Utility Files
DATA_LOADER_FILE = os.path.join(UTILS_DIR, 'data_loader.py')
WEATHER_SIM_FILE = os.path.join(UTILS_DIR, 'weather_simulator.py')

# Weather Settings
SEASON_TEMPS = {
    'winter': (20, 40),
    'spring': (45, 70),
    'summer': (70, 95),
    'autumn': (40, 65)
}

WEATHER_PROBS = {
    'winter': {'sunny': 0.3, 'cloudy': 0.4, 'rainy': 0.1, 'snow': 0.2},
    'summer': {'sunny': 0.7, 'cloudy': 0.2, 'rainy': 0.1, 'snow': 0.0},
    'spring': {'sunny': 0.4, 'cloudy': 0.3, 'rainy': 0.3, 'snow': 0.0},
    'autumn': {'sunny': 0.3, 'cloudy': 0.4, 'rainy': 0.3, 'snow': 0.0}
}


'''
Key Components
USE_FAHRENHEIT: Global flag for temperature units

Path configurations for organized file storage

Weather simulation parameters:

Temperature ranges by season

Weather probability distributions

Verification
All paths use os.path.join() for cross-platform compatibility

Season temperatures reflect your request (summer hotter than winter)

Weather probabilities make logical sense (more snow in winter)
'''
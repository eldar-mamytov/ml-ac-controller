from pathlib import Path

# Temperature Unit (Fahrenheit)
USE_FAHRENHEIT = True

# Base Directory (points to ml-ac-controller/)
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Goes up 3 levels from app/core/

# Directory Paths (all relative to BASE_DIR)
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"      # Now directly under root
SCHEMAS_DIR = BASE_DIR / "schemas"    # Now directly under root
UTILS_DIR = BASE_DIR / "utils"        # Now directly under root
LOGS_DIR = BASE_DIR / "logs"
REPORTS_DIR = BASE_DIR / "reports"

# File Paths
DATA_FILE = DATA_DIR / "ac_data.csv"
MODEL_FILE = MODELS_DIR / "ac_model.joblib"
SCHEMA_FILE = SCHEMAS_DIR / "data_schemas.py"
DATA_LOADER_FILE = UTILS_DIR / "data_loader.py"
WEATHER_SIM_FILE = UTILS_DIR / "weather_simulation.py"  # Fixed filename to match your structure
LOG_FILE = LOGS_DIR / "error.log"

# Weather Settings (unchanged)
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

# Create directories if missing (no error if exists)
for dir_path in [DATA_DIR, MODELS_DIR, SCHEMAS_DIR, UTILS_DIR, LOGS_DIR, REPORTS_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)
# ml-ac-controller/test_imports.py
try:
    from schemas.data_schemas import ACDataPoint
    from app.core.config import DATA_FILE
    from utils.weather_simulation import generate_weather
    print("✅ All imports work correctly!")
except ImportError as e:
    print(f"❌ Import failed: {e}")
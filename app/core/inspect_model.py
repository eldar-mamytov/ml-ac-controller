from joblib import load
from pathlib import Path
from config import MODEL_FILE

# Load the model
model = load(MODEL_FILE)

# Print model details
print("\nModel Parameters:")
print(model.get_params())

# If its a RandomForestClassifier
if hasattr(model, "feature_importances_"):
    print("\nFeature Importances:")
    print(model.feature_importances_)
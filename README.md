ML-AC-Controller

An intelligent, interactive AC controller system powered by machine learning. This project simulates seasonal weather conditions, generates synthetic data, trains a classifier, and provides predictions based on real-time user inputs (temperature, humidity, season, occupancy, and weather). Ideal for demonstrating data science pipelines with real-world context.

⸻

Features
	•	Synthetic Data Generation for AC behavior using seasonal weather patterns
	•	Random Forest Classifier trained on labeled AC usage scenarios
	•	Smart Prediction System for real-time AC recommendations
	•	Clean CLI Interface for user interaction
	•	Validation with Pydantic to ensure realistic inputs
	•	Data Visualizations for feature importances and distributions

⸻

Project Structure

ml-ac-controller/
├── app/
│   ├── core/
│   │   ├── config.py              # Configuration constants and paths
│   │   ├── generate_data.py       # Synthetic data generator
│   │   ├── train_model.py         # Model training and evaluation
│   │   ├── predict.py             # User CLI prediction script
│   │   ├── inspect_model.py       # Inspect saved model internals
│   │   └── visualize.py           # Plot feature importances
│   ├── models/
│   │   └── ac_model.joblib        # Trained Random Forest model
│   ├── schemas/
│   │   └── data_schemas.py        # Pydantic schema validation
│   └── utils/
│       ├── data_loader.py         # Helper for loading data
│       └── weather_simulation.py  # Seasonal weather generator
├── data/
│   └── ac_data.csv                # Generated dataset
├── reports/
│   └── *.png                      # Visualizations
├── logs/
│   └── error.log                  # Error logs
├── requirements.txt               # Python dependencies
├── setup.py                       # Python packaging setup
└── README.md


⸻

⚙️ Installation

# Clone the repository
$ git clone https://github.com/eldar-mamytov/ml-ac-controller.git
$ cd ml-ac-controller

# Create virtual environment
$ python3 -m venv venv
$ source venv/bin/activate  # For Windows: .\venv\Scripts\activate

# Install dependencies
$ pip install -r requirements.txt


⸻

How It Works

1. Generate Data

python app/core/generate_data.py

Creates a realistic dataset of AC usage behavior stored in data/ac_data.csv.

2. Train the Model

python app/core/train_model.py

Trains a RandomForestClassifier on the synthetic dataset. Outputs:
	•	Accuracy and classification report
	•	Trained model saved to models/ac_model.joblib

3. Make Predictions

python app/core/predict.py

Runs a command-line interface where the user enters:
	•	Temperature
	•	Humidity
	•	Season (winter/spring/summer/autumn)
	•	Weather (sunny/cloudy/rainy/snow)
	•	Occupancy

Outputs a prediction: whether AC should be ON or OFF and the model’s confidence.

4. Visualize Results

python app/core/visualize.py

Generates plots showing:
	•	Feature importance
	•	Data distributions

⸻

✅ Example

--- AC State Predictor ---
Current temperature (°F): 81
Humidity (%): 70
Season (winter/spring/summer/autumn): summer
Number of people in room: 1
Weather (sunny/cloudy/rainy/snow): sunny

Prediction: AC should be On (confidence: 96.5%)


⸻

📦 Dependencies
	•	Python 3.8+
	•	pandas, numpy, matplotlib, seaborn
	•	scikit-learn, joblib
	•	pydantic (v2)

Install them with:

pip install -r requirements.txt


⸻

✍️ Author

Created by [Your Name]. Contributions welcome!

⸻

📄 License

This project is licensed under the MIT License. See LICENSE for details.
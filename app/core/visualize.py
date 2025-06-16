import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import pandas as pd
from pathlib import Path
from config import MODEL_FILE, DATA_FILE

# Generates feature importance plot
def plot_feature_importance():
    model = joblib.load(MODEL_FILE)
    features = model.feature_names_in_
    importance = model.feature_importances_
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=importance, y=features, palette="Blues_d")
    sns.barplot(x=importance, y=features, hue=features, palette="Blues_d", legend=False, dodge=False)
    plt.tight_layout()
    plt.savefig("reports/feature_importance.png")
    plt.show()


# Creates distribution plots for key features
def plot_data_distribution():
    df = pd.read_csv(DATA_FILE)
    
    plt.figure(figsize=(12, 8))
    
    # Temperature distribution
    plt.subplot(2, 2, 1)
    sns.histplot(df['temperature'], bins=20, kde=True)
    plt.title("Temperature Distribution")
    
    # AC State by Season
    plt.subplot(2, 2, 2)
    sns.countplot(data=df, x='season', hue='ac_state')
    plt.title("AC Usage by Season")
    
    plt.tight_layout()
    plt.savefig("reports/data_distributions.png")

if __name__ == "__main__":
    Path("reports").mkdir(exist_ok=True)
    plot_feature_importance()
    plot_data_distribution()
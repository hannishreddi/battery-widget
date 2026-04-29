import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# Load data
df = pd.read_csv("data.csv")

# Encode context
le = LabelEncoder()
df["context"] = le.fit_transform(df["context"])

# Features & target
X = df[["cpu", "ram", "battery", "plugged", "context"]]
y = df["drain"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model + encoder
joblib.dump(model, "model.pkl")
joblib.dump(le, "encoder.pkl")

print("Model trained successfully!")
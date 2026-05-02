import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib

# Load data
df = pd.read_csv("data.csv")

# Encode context
le = LabelEncoder()
df["context"] = le.fit_transform(df["context"])

# Features & target
X = df[[
    "cpu", "ram", "battery", "plugged",
    "processes", "net_sent", "net_recv",
    "top_cpu", "context"
]]

y = df["drain"]

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Save model + encoder
joblib.dump(model, "model.pkl")
joblib.dump(le, "encoder.pkl")

print("Model trained successfully!")
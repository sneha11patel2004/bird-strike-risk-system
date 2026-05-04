import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# Load data
data = pd.read_csv("data/risk_data.csv")

# Encoders
le_b = LabelEncoder()
le_d = LabelEncoder()
le_z = LabelEncoder()
le_m = LabelEncoder()
le_w = LabelEncoder()
le_t = LabelEncoder()
le_r = LabelEncoder()

# Encode columns
data["behaviour"] = le_b.fit_transform(data["behaviour"])
data["density"] = le_d.fit_transform(data["density"])
data["runway_zone"] = le_z.fit_transform(data["runway_zone"])
data["body_mass"] = le_m.fit_transform(data["body_mass"])
data["weather"] = le_w.fit_transform(data["weather"])
data["time"] = le_t.fit_transform(data["time"])
data["risk"] = le_r.fit_transform(data["risk"])

# Features + target
X = data[["bird_count","behaviour","density","runway_zone","body_mass","weather","time"]]
y = data["risk"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open("models/risk_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save encoders
with open("models/encoders.pkl", "wb") as f:
    pickle.dump({
        "behaviour": le_b,
        "density": le_d,
        "zone": le_z,
        "mass": le_m,
        "weather": le_w,
        "time": le_t,
        "risk": le_r
    }, f)

print("Model trained and saved!")
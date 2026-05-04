import pickle

# Load trained model
with open("models/risk_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load encoders
with open("models/encoders.pkl", "rb") as f:
    encoders = pickle.load(f)


def predict_risk(bird_count, behaviour, density, zone):

    # Default values (since not coming from frontend)
    weather = "windy"
    time = "morning"

    # Body mass logic
    if bird_count >= 7:
        body_mass = "large"
    elif bird_count >= 3:
        body_mass = "medium"
    else:
        body_mass = "small"

    # 🔥 ENCODING (THIS WAS MISSING IN YOUR CODE)
    inp = [[
        bird_count,
        encoders["behaviour"].transform([behaviour])[0],
        encoders["density"].transform([density])[0],
        encoders["zone"].transform([zone])[0],
        encoders["mass"].transform([body_mass])[0],
        encoders["weather"].transform([weather])[0],
        encoders["time"].transform([time])[0]
    ]]

    # Prediction
    pred = model.predict(inp)

    # Convert back to label
    return encoders["risk"].inverse_transform(pred)[0]


# 🔷 Explanation
def explain_risk(density, zone, behaviour):
    if density == "high" and zone == "high":
        return "High ecological risk due to dense flock near runway"
    elif behaviour == "crossing":
        return "Moderate ecological risk due to birds crossing flight path"
    elif density == "medium":
        return "Moderate risk due to bird activity"
    else:
        return "Low ecological risk"


# 🔷 Risk score
def risk_score(bird_count, density, zone):
    score = bird_count * 2

    if density == "high":
        score += 5
    elif density == "medium":
        score += 2

    if zone == "high":
        score += 5
    elif zone == "medium":
        score += 2

    return score


# 🔷 Confidence
def confidence_score(score):
    if score >= 15:
        return 0.9
    elif score >= 10:
        return 0.7
    else:
        return 0.5
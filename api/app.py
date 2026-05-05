import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, request, jsonify

app = Flask(__name__)

from utils.video import extract_frames
from detection.detect import get_positions
from behaviour.movement import get_behaviour_sequence, get_density, get_runway_zone
from prediction.model import predict_risk, explain_risk, risk_score, confidence_score


@app.route("/")
def home():
    return "Bird Strike Risk API is running"


@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "video" not in request.files:
            return jsonify({"error": "No video uploaded"}), 400

        video = request.files["video"]

        if video.filename == "":
            return jsonify({"error": "Empty video file"}), 400

        video_path = "input.mp4"
        video.save(video_path)

        frame_files = extract_frames(video_path)

        if not frame_files:
            return jsonify({"error": "No frames extracted"}), 400

        frames_positions = []
        for f in frame_files:
            positions = get_positions(f)
            frames_positions.append(positions)

        last_frame = frames_positions[-1]
        bird_count = len(last_frame)

        behaviour = get_behaviour_sequence(frames_positions)
        density = get_density(last_frame)
        zone = get_runway_zone(last_frame, 800)

        risk = predict_risk(bird_count, behaviour, density, zone)

        score = risk_score(bird_count, density, zone)
        confidence = confidence_score(score)
        explanation = explain_risk(density, zone, behaviour)

        return jsonify({
            "bird_count": bird_count,
            "behaviour": behaviour,
            "density": density,
            "runway_zone": zone,
            "risk_level": risk,
            "risk_score": score,
            "confidence": confidence,
            "explanation": explanation
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
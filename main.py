from detection.detect import get_positions
from behaviour.movement import get_behaviour
from prediction.model import predict_risk

frame1 = get_positions("data/frame1.jpg")
frame2 = get_positions("data/frame2.jpg")

bird_count = len(frame2)
behaviour = get_behaviour(frame1, frame2)

risk = predict_risk(bird_count, behaviour)

print("\n===== FINAL OUTPUT =====")
print("Bird Count:", bird_count)
print("Behaviour:", behaviour)
print("Risk:", risk)
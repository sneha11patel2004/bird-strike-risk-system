from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.pt")

# Run detection
results = model("data/test.jpg")

boxes = results[0].boxes

bird_count = 0
positions = []

for box in boxes:
    cls = int(box.cls[0])  # class id

    # COCO class 14 = bird
    if cls == 14:
        bird_count += 1

        x1, y1, x2, y2 = box.xyxy[0]

        # centroid
        cx = (x1 + x2) / 2
        cy = (y1 + y2) / 2

        positions.append((float(cx), float(cy)))

print("Bird Count:", bird_count)
print("Positions:", positions)
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def get_positions(image_path):
    results = model(image_path)
    boxes = results[0].boxes

    positions = []

    for box in boxes:
        if int(box.cls[0]) == 14:
            x1, y1, x2, y2 = box.xyxy[0]
            cx = (x1 + x2) / 2
            cy = (y1 + y2) / 2
            positions.append((float(cx), float(cy)))

    return positions
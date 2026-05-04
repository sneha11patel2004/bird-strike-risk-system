import cv2

def extract_frames(video_path):
    cap = cv2.VideoCapture(video_path)

    frames = []
    count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # sample every 10 frames (adjustable)
        if count % 10 == 0:
            filename = f"temp_{count}.jpg"
            cv2.imwrite(filename, frame)
            frames.append(filename)

        count += 1

    cap.release()
    return frames
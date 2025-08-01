import cv2
from ultralytics import YOLO
from playsound import playsound
import threading

# Load YOLOv8 model
model = YOLO("yolo_weights/yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

# Define restricted zone (x1, y1, x2, y2)
restricted_zone = (50, 50, 200, 100)

def play_alert():
    playsound('sound.mp3')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]

    for box in results.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        label = model.names[cls_id]
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        # Draw bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(frame, f'{label} {conf:.2f}', (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        # Check if person enters restricted zone
        if label == 'person':
            rx1, ry1, rx2, ry2 = restricted_zone

            # Calculate intersection area between person and restricted zone
            ix1 = max(x1, rx1)
            iy1 = max(y1, ry1)
            ix2 = min(x2, rx2)
            iy2 = min(y2, ry2)

            # Check if there is an actual overlapping area
            if ix1 < ix2 and iy1 < iy2:
                cv2.putText(frame, "INTRUSION DETECTED!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
                threading.Thread(target=play_alert).start()


    # Draw restricted zone
    cv2.rectangle(frame, restricted_zone[:2], restricted_zone[2:], (0, 0, 255), 2)

    # Show the frame
    cv2.imshow("Surveillance Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

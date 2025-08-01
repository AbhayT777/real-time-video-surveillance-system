
#  Real-Time Video Surveillance System

A Python-based real-time surveillance system that uses **YOLOv8** for object detection and automatically triggers alerts when a person is detected entering a **restricted zone** in a live video feed.

---

##  Features

-  **Intrusion Detection** using YOLOv8
-  **Customizable Restricted Zones**
-  **Real-Time Alerts** via audio notification (`alert.mp3`)
-  Supports **live webcam** feed
-  Lightweight, simple, and fast

---

##  Tech Stack

- **Python**
- **OpenCV**
- **YOLOv8 (Ultralytics)**
- **cvzone**
- **Pygame** (for audio alert)

---

##  How It Works

1. The script captures video from your **webcam**.
2. Each frame is passed to **YOLOv8**, which detects objects like `person`.
3. If a person is detected **inside a predefined restricted zone**, the system:
   - Displays an **"INTRUSION DETECTED"** warning on the screen
   - Plays an **audio alert (`sound.mp3`)** in a separate thread
4. The alert can repeat as long as the person remains in the zone.

---

##  Project Structure

```
real-time-video-surveillance-system/
│
├── surveillance.py         # Main application script
├── requirements.txt        # Python dependencies
├── sound.mp3               # Audio alert played on intrusion
├── yolo_weights/           # YOLOv8 weights directory
│   └── yolov8n.pt          # Pretrained YOLOv8 model (nano version)
└── README.md               # Project documentation
```

---

##  Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/real-time-video-surveillance-system.git
cd real-time-video-surveillance-system
```

2. **Create a virtual environment:**

```bash
python -m venv surveillance_venv
surveillance_venv\Scripts\activate  # For Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Download YOLOv8 weights:**

```bash
pip install ultralytics
yolo export model=yolov8n.pt format=pt  # Optional if not included
```

5. **Run the script:**

```bash
python surveillance.py
```

---

##  How to Stop the Script

The script runs continuously using your webcam. To stop:

- Press `Q` in the video window  
OR  
- Use `Ctrl+C` in the terminal

---

##  Customization

- **Change Restricted Zone**: Modify the `restricted_zone = (x1, y1, x2, y2)` tuple in `surveillance.py`
- **Change Alert Sound**: Replace `sound.mp3` with your custom sound file (keep the filename or update it in the code)

---



##  Author

**Abhay Kumar Tiwari**  
[GitHub](https://github.com/AbhayT777) • [LinkedIn](https://www.linkedin.com/in/abhay-kumar-tiwari-0191a6121/)

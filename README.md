# DroneFaceDetection 🚁

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/izeeshanahmedkhan/DroneFaceDetection)

## 📝 Project Summary

DroneFaceDetection is an intelligent surveillance system that combines real-time face detection and recognition with automated email notification capabilities. The system captures video feed from a camera (drone or webcam), identifies known faces, and sends instant email alerts with location information when faces are detected.

## 🎯 Purpose

This project was designed to enhance security and surveillance capabilities by:
- Enabling real-time face detection and recognition from drone or fixed cameras
- Providing automated notifications when specific individuals are detected
- Creating a scalable training system for adding new faces to the recognition database
- Supporting remote monitoring through email alerts with geolocation data

## 🛠️ Tech Stack

- **Python 3.6+**: Core programming language
- **OpenCV (cv2)**: Computer vision and face detection/recognition
- **NumPy**: Numerical operations and data processing
- **PIL (Pillow)**: Image processing
- **smtplib**: Email notification system
- **Haarcascade Classifier**: Face detection algorithm
- **LBPH Face Recognizer**: Local Binary Patterns Histograms for face recognition

## 📦 Installation & Setup

### Prerequisites

```bash
# Python 3.6 or higher
python --version
```

### Step 1: Clone the Repository

```bash
git clone https://github.com/izeeshanahmedkhan/DroneFaceDetection.git
cd DroneFaceDetection
```

### Step 2: Install Dependencies

```bash
pip install opencv-python
pip install opencv-contrib-python
pip install numpy
pip install pillow
```

Or install all at once:

```bash
pip install opencv-python opencv-contrib-python numpy pillow
```

### Step 3: Configure Email Notifications

Edit the `mail.py` file to add your email credentials:

```python
server.login("your_email@gmail.com", "your_password")
msg['From'] = "your_email@gmail.com"
msg['To'] = "recipient@gmail.com"
```

**Security Note**: For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833) instead of your regular password.

### Step 4: Prepare Dataset

Create a directory structure:

```
DroneFaceDetection/
├── dataSet/
│   └── (face images will be stored here)
├── trainer/
│   └── (trained model will be saved here)
```

## 🚀 Usage

### 1. Collect Face Data

Run the dataset collection script to capture face samples:

```bash
python face_datasets.py
```

- Enter the user ID when prompted
- Look at the camera, the system will capture 20 sample images
- Images are saved in the `dataSet` directory

### 2. Train the Model

Train the face recognition model with collected data:

```bash
python training.py
```

This creates a `trainer.yml` file in the `trainer` directory containing the trained model.

### 3. Run Face Recognition

Start the face recognition system:

```bash
python face_recognition.py
```

- The system will start video capture
- Detected faces will be highlighted with rectangles
- Recognized faces trigger email notifications with:
  - Detection timestamp
  - Person ID
  - Confidence level
  - GPS coordinates (if available)

## 📸 Features

- ✅ Real-time face detection using Haarcascade classifier
- ✅ Face recognition with confidence scoring
- ✅ Automated email alerts with detection details
- ✅ Scalable training system for multiple users
- ✅ Support for both webcam and drone camera feeds
- ✅ Location tracking integration
- ✅ Confidence threshold filtering to reduce false positives

## 📊 System Architecture

```
┌─────────────────┐
│  Camera Feed    │
│ (Drone/Webcam)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Face Detection  │
│  (Haarcascade)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Face         │
│  Recognition    │
│     (LBPH)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     Email       │
│  Notification   │
└─────────────────┘
```

## 📁 Project Structure

```
DroneFaceDetection/
│
├── face_datasets.py          # Collect face samples for training
├── training.py                # Train the face recognition model
├── face_recognition.py        # Main recognition and detection system
├── mail.py                    # Email notification module
├── haarcascade_frontalface_default.xml  # Face detection classifier
│
├── dataSet/                   # Stores captured face images
│   └── User.[id].[n].jpg
│
└── trainer/                   # Stores trained model
    └── trainer.yml
```

## ⚙️ Configuration

### Detection Parameters

You can adjust detection sensitivity in `face_recognition.py`:

```python
# Confidence threshold (lower = stricter)
if confidence < 100:
    # Face recognized
```

### Camera Source

Change the video source in `face_recognition.py`:

```python
cam = cv2.VideoCapture(0)  # 0 for default webcam
# or
cam = cv2.VideoCapture('http://drone_ip/video')  # For drone camera
```

## 🔒 Security Considerations

- **Never commit credentials**: Keep email credentials in environment variables
- **Use App Passwords**: For Gmail, generate app-specific passwords
- **Secure storage**: Store trained models securely
- **Privacy compliance**: Ensure compliance with local privacy laws when deploying surveillance systems

## 🐛 Troubleshooting

### Camera not detected
```bash
# Try different camera indices
cam = cv2.VideoCapture(1)  # or 2, 3, etc.
```

### Email not sending
- Verify email credentials
- Enable "Less secure app access" or use App Password for Gmail
- Check firewall settings

### Low recognition accuracy
- Collect more diverse face samples (different angles, lighting)
- Ensure good lighting conditions during capture
- Increase the number of training samples per person

## 📈 Future Enhancements

- [ ] Support for multiple simultaneous face recognition
- [ ] Integration with cloud storage for face datasets
- [ ] Mobile app for remote monitoring
- [ ] Support for deep learning models (YOLO, SSD)
- [ ] Database integration for logging detections
- [ ] Web dashboard for system management

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Izeeshan Ahmed Khan**
- GitHub: [@izeeshanahmedkhan](https://github.com/izeeshanahmedkhan)

## 🙏 Acknowledgments

- OpenCV community for the excellent computer vision library
- Haarcascade classifier for robust face detection
- LBPH algorithm for efficient face recognition

---

⭐ If you find this project useful, please consider giving it a star!

<h1>🦯 Smart Blind Stick</h1>
💻 AI + IoT Based Assistive Technology for Visually Impaired People
📌 Overview
The Smart Blind Stick is an AI + IoT based assistive technology project designed for visually impaired individuals.

Unlike traditional white canes, this smart stick can:

✅ Detect nearby obstacles
✅ Alert using buzzer + vibration
✅ Detect danger distance levels
✅ Track live GPS location
✅ Trigger geofence alerts
✅ Send Google Maps location link
This project combines Arduino, Ultrasonic Sensors, GPS Tracking, and Python Software to create a low-cost smart navigation system.

🚨 Problem Statement
Traditional blind sticks only detect ground-level obstacles and provide limited assistance.

They cannot:

❌ Detect chest/head-level obstacles
❌ Identify danger distance levels
❌ Track user location
❌ Alert caretakers when user leaves a safe zone
This creates serious safety risks for visually impaired users.

💡 Proposed Solution
The Smart Blind Stick solves these issues using:

📡 HC-SR04 ultrasonic sensor for obstacle detection

🔊 Buzzer + vibration motor for alerts
📍 NEO-6M GPS module for live tracking
🖥️ Python software for geofence monitoring
🌍 Google Maps location sharing
⚙️ Features

🧠 Smart Obstacle Detection
Detects obstacles within 100 cm
Real-time distance monitoring
Fast response alerts
🔊 Intelligent Buzzer Alerts
Works like a car parking sensor:

Distance	Alert Type
>100 cm	Silent
60–100 cm	Slow beep
30–60 cm	Medium beep
10–30 cm	Fast beep
<10 cm	Continuous beep

📳 Vibration Feedback
Provides haptic feedback
Improves accessibility in noisy environments

📍 GPS Tracking
Real-time user location tracking
Accurate coordinate monitoring
🛑 Geofence Alert System
If the user moves beyond 100 metres from home:

🚨 Dark popup appears on laptop
📍 Shows live coordinates
🌍 Shows Google Maps link
📌 Always-on-top emergency alert window
🛠️ Hardware Components
Component	Quantity
Arduino Uno R3	1
HC-SR04 Ultrasonic Sensor	1
Piezo Buzzer	1
Coin Vibration Motor	1
BC547 NPN Transistor	1
1k Ohm Resistor	1
NEO-6M GPS Module	1
Breadboard	1
Jumper Wires	Multiple
9V Battery	1
PVC Stick	1
🔌 Circuit Connections
HC-SR04 Connections
Sensor Pin	Arduino Pin
VCC	5V
GND	GND
TRIG	Pin 9
ECHO	Pin 10
🔊 Buzzer Connections
Buzzer Pin	Arduino Pin
Positive	Pin 8
Negative	GND
📳 Vibration Motor Connections
Motor Pin	Arduino Pin
Positive	Pin 7
Negative	GND
📍 GPS Module Connections
GPS Pin	Arduino Pin
VCC	3.3V
GND	GND
TX	Pin 4
RX	Pin 3
⚠️ Important: NEO-6M GPS module should be connected to 3.3V ONLY

🧮 Working Principle
📏 Ultrasonic Distance Formula
d = (t × 0.034) / 2
Where:

d = distance in cm
t = echo time duration
🌍 GPS Distance Calculation
The project uses the Haversine Formula to calculate real-world distance between two GPS coordinates.

Used for:

📍 Safe zone detection
🚨 Geofence alerts
📡 Live tracking
💻 Software Stack
Software	Purpose
Arduino IDE	Arduino programming
Python 3.11	GPS + popup logic
VS Code	Code editor
pyserial	Serial communication
tkinter	GUI popup alerts
📂 Project Structure
Smart-Blind-Stick/
│
├── Arduino/
│   └── blind_stick.ino
│
├── Python/
│   └── main.py
│
├── Images/
│   ├── circuit_diagram.png
│   ├── prototype.jpg
│   └── popup_alert.png
│
├── README.md
└── requirements.txt
🧾 Arduino Responsibilities
blind_stick.ino
Handles:

Ultrasonic sensor reading
Distance calculation
Buzzer patterns
Vibration motor control
GPS serial transmission
🖥️ Python Responsibilities
main.py
Handles:

Reading serial data
Parsing GPS NMEA data
Haversine calculations
Geofence monitoring
Popup alert generation
Google Maps link creation
🚨 Popup Alert System
🌑 Dark-Themed Emergency Popup
Displays:

🚨 GEOFENCE ALERT
📍 Latitude & Longitude
🌍 Google Maps Link
✅ OK Acknowledged Button
Features
Always-on-top popup
Red emergency warning header
Emergency-style UI
🔮 Future Scope
🚀 Raspberry Pi standalone version
📱 Android caretaker mobile app
💧 Water puddle detection sensor
🧠 AI object recognition using YOLOv5
📡 GSM emergency SMS alerts
📷 Camera-based navigation assistance
🎙️ Voice assistant integration
☁️ Live cloud tracking dashboard
📈 Applications
🦯 Blind navigation assistance
🏥 Smart healthcare systems
👴 Elderly safety monitoring
🧭 Indoor & outdoor navigation
🤖 Assistive robotics

🧑‍💻 Author

👨‍💻 Developed By

Trushna Dinesh Kundale

⭐ Support
If you like this project:

⭐ Star the repository
🍴 Fork the project
📢 Share with others

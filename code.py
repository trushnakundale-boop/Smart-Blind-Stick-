import serial
import time
import math
import threading
import tkinter as tk
from tkinter import font

ARDUINO_PORT = "COM3"
BAUD_RATE = 115200

HOME_LAT = 19.843127064527124
HOME_LON = 75.2423639173283
SAFE_RADIUS = 30

last_alert_time = 0
ALERT_COOLDOWN = 30

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000
    p1 = math.radians(lat1)
    p2 = math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = (math.sin(dp/2)**2 +
         math.cos(p1) * math.cos(p2) *
         math.sin(dl/2)**2)
    return R * 2 * math.atan2(
        math.sqrt(a), math.sqrt(1-a))

def parse_gps(line):
    try:
        if "$GPRMC" in line:
            p = line.split(",")
            if p[2] == "A":
                lat = (float(p[3][:2]) +
                       float(p[3][2:])/60)
                lon = (float(p[5][:3]) +
                       float(p[5][3:])/60)
                return lat, lon
    except:
        pass
    return None, None

def show_popup(lat, lon):
    # Bootstrap jaisa dark popup
    root = tk.Tk()
    root.title("Smart Blind Stick Alert")
    root.configure(bg="#212529")
    root.resizable(False, False)

    # Center screen pe
    w, h = 420, 320
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw // 2) - (w // 2)
    y = (sh // 2) - (h // 2)
    root.geometry(f"{w}x{h}+{x}+{y}")

    # Always on top
    root.attributes("-topmost", True)

    # Header
    header = tk.Frame(root, bg="#dc3545", height=50)
    header.pack(fill="x")
    header.pack_propagate(False)

    tk.Label(
        header,
        text="⚠️  GEOFENCE ALERT",
        bg="#dc3545",
        fg="white",
        font=("Segoe UI", 14, "bold")
    ).pack(expand=True)

    # Body
    body = tk.Frame(root, bg="#212529", pady=15)
    body.pack(fill="both", expand=True, padx=20)

    tk.Label(
        body,
        text="🚨 User has left the safe zone!",
        bg="#212529",
        fg="white",
        font=("Segoe UI", 12, "bold")
    ).pack(anchor="w", pady=(0, 15))

    # Location box
    loc_frame = tk.Frame(body, bg="#343a40",
                         padx=10, pady=10)
    loc_frame.pack(fill="x", pady=(0, 10))

    tk.Label(
        loc_frame,
        text="📍 Location:",
        bg="#343a40",
        fg="#adb5bd",
        font=("Segoe UI", 9, "bold")
    ).pack(anchor="w")

    tk.Label(
        loc_frame,
        text=f"Lat: {lat:.6f}",
        bg="#343a40",
        fg="white",
        font=("Segoe UI", 10)
    ).pack(anchor="w")

    tk.Label(
        loc_frame,
        text=f"Lon: {lon:.6f}",
        bg="#343a40",
        fg="white",
        font=("Segoe UI", 10)
    ).pack(anchor="w")

    maps_link = f"maps.google.com/?q={lat},{lon}"
    tk.Label(
        loc_frame,
        text=f"🗺️  {maps_link}",
        bg="#343a40",
        fg="#0d6efd",
        font=("Segoe UI", 9),
        cursor="hand2"
    ).pack(anchor="w", pady=(5, 0))

    # OK Button
    btn_frame = tk.Frame(root, bg="#212529",
                         pady=10)
    btn_frame.pack(fill="x", padx=20)

    tk.Button(
        btn_frame,
        text="OK — Acknowledged",
        bg="#dc3545",
        fg="white",
        font=("Segoe UI", 11, "bold"),
        relief="flat",
        padx=20,
        pady=8,
        cursor="hand2",
        command=root.destroy
    ).pack(fill="x")

    root.mainloop()

def main():
    global last_alert_time

    print("🚀 Smart Blind Stick Starting...")

    try:
        arduino = serial.Serial(
            ARDUINO_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)
        print("✅ Arduino Connected!")
    except:
        print("❌ Arduino not found!")
        print("Check COM port!")
        return

    print("📍 Monitoring started...")
    print("-" * 40)

    while True:
        try:
            line = arduino.readline().decode(
                "utf-8", errors="ignore").strip()

            if not line:
                continue

            if line.startswith("DIST:"):
                dist = float(line.replace("DIST:", ""))
                if dist != 400:
                    print(f"📏 Distance: {dist:.1f} cm")
                    if dist > 60:
                        print("⚠️  FAR — Object detected")
                    elif dist > 30:
                        print("🟠 NEAR — Slow down!")
                    elif dist > 10:
                        print("🔴 DANGER — Stop!")
                    else:
                        print("🚨 CRITICAL!")
                else:
                    print("✅ SAFE — No obstacle")

            lat, lon = parse_gps(line)
            if lat and lon:
                print(f"📡 GPS: {lat:.6f}, {lon:.6f}")
                dist_home = haversine(
                    HOME_LAT, HOME_LON, lat, lon)
                print(f"🏠 From home: {dist_home:.1f}m")

                now = time.time()
                if (dist_home > SAFE_RADIUS and
                        now - last_alert_time > ALERT_COOLDOWN):
                    print("🚨 ALERT! User left safe zone!")
                    last_alert_time = now
                    threading.Thread(
                        target=show_popup,
                        args=(lat, lon),
                        daemon=True
                    ).start()

        except KeyboardInterrupt:
            print("\n🛑 System stopped!")
            break
        except Exception as e:
            continue

if __name__ == "__main__":
    main()
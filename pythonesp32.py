 

# WiFi credentials
SSID = "Mindnics"
PASSWORD = "Mindnics"

# Firebase settings
API_KEY = "AIzaSyBDzr5UFL4VsCbjEPKcopyGAFXFCnbrUB0"
DATABASE_URL = "https://soil-monitoring-sensor-dcb9d-default-rtdb.firebaseio.com/"

# Initialize UART for RS485 (Modbus)
uart = UART(2, baudrate=9600, tx=17, rx=16)

# Connect to WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)
while not wifi.isconnected():
    print("Connecting to WiFi...")
    time.sleep(1)
print("Connected:", wifi.ifconfig())

# Dummy sensor read functions (replace with Modbus read logic)
def read_ph(): return 6.5
def read_moisture(): return 45.2
def read_temp(): return 28.4
def read_conductivity(): return 120
def read_npk(): return (30, 20, 15)

# Upload to Firebase
def upload_data():
    timestamp = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
    data = {
        "pH": f"{read_ph()} pH",
        "soil_moisture": f"{read_moisture()} %",
        "temperature": f"{read_temp()} C",
        "conductivity": f"{read_conductivity()} us/cm",
        "Nitrogen": f"{read_npk()[0]} mg/kg",
        "Phosphorus": f"{read_npk()[1]} mg/kg",
        "Potassium": f"{read_npk()[2]} mg/kg"
    }
    url = DATABASE_URL + "/sensor_logs/" + timestamp + ".json"
    try:
        res = urequests.put(url, data=json.dumps(data))
        print("Uploaded:", res.status_code)
        res.close()
    except Exception as e:
        print("Upload failed:", e)

# Main loop
while True:
    upload_data()
    utime.sleep(10)  # Upload every 10 seconds



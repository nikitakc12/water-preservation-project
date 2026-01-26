from machine import ADC
import network
import utime
import ntptime
import urequests

# ----- ADC pin setup -----
ph_adc = ADC(1)      # GP27 (pH)
tds_adc = ADC(0)     # GP26 (TDS)

# ----- WiFi credentials -----
SSID = "Numaer iPhone"
PASSWORD = "123456789"

# ----- ThingSpeak API -----
THINGSPEAK_WRITE_KEY = "8X4F1EFZV0PIP1CJ"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# ----- Connect to WiFi -----
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(ssid, password)

        while not wlan.isconnected():
            utime.sleep(1)

    print("Connected! IP:", wlan.ifconfig()[0])
    return wlan

wlan = connect_wifi(SSID, PASSWORD)

# ----- Sync time -----
print("Syncing time with NTP...")
try:
    ntptime.settime()
    print("Time synced!")
except:
    print("NTP sync failed, using internal clock")

# ----- Sensor helpers -----
def read_voltage(adc):
    raw = adc.read_u16()
    voltage = (raw / 65535) * 3.3
    return voltage

def get_ph(voltage):
    return (14 / 3.0) * voltage   # simple approx, works for now

def get_tds(voltage):
    return (voltage * 1000) / 2.3  # approx for Grove sensor

def get_conductivity(tds):
    return tds * 2   # µS/cm — typical conversion

def get_time_string():
    t = utime.localtime()
    return "{:02d}:{:02d}:{:02d}".format(t[3], t[4], t[5])

# ----- Main Loop -----
while True:
    ph_voltage = read_voltage(ph_adc)
    tds_voltage = read_voltage(tds_adc)

    ph_value = get_ph(ph_voltage)
    tds_value = get_tds(tds_voltage)
    cond_value = get_conductivity(tds_value)

    timestamp = get_time_string()

    print("Time:", timestamp)
    print("pH ≈ {:.2f}".format(ph_value))
    print("TDS ≈ {:.0f} ppm".format(tds_value))
    print("Conductivity ≈ {:.0f} µS/cm".format(cond_value))
    print("---------------------------------------")

    # Send to ThingSpeak
    try:
        url = (
            THINGSPEAK_URL +
            "?api_key={}&field1={:.2f}&field2={:.0f}&field3={:.0f}".format(
                THINGSPEAK_WRITE_KEY, ph_value, tds_value, cond_value
            )
        )
        response = urequests.get(url)
        response.close()
        print("Data sent to ThingSpeak!")
    except Exception as e:
        print("Failed to send:", e)

    utime.sleep(30)  # ThingSpeak minimum interval for free accounts


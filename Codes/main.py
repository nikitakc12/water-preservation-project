from machine import SPI, Pin, ADC, RTC
import network, utime, ntptime, urequests
import sdcard, uos

# ── WiFi credentials ───────────────────────────────────────
SSID     = "Numaer iPhone"
PASSWORD = "123456789"

# ── ThingSpeak ─────────────────────────────────────────────
THINGSPEAK_WRITE_KEY = "8X4F1EFZV0PIP1CJ"
THINGSPEAK_URL       = "https://api.thingspeak.com/update"

# ── Sensor pins ────────────────────────────────────────────
ph_adc  = ADC(Pin(27))  # pH  on GP27 (ADC1)
tds_adc = ADC(Pin(26))  # TDS on GP26 (ADC0)

# ── Calibration constants ──────────────────────────────────
PH_M  = 11.03   # pH  = PH_M * voltage + PH_B
PH_B  = -6.06
TDS_K = 302.1   # TDS = TDS_K * voltage

# ── SD card setup ──────────────────────────────────────────
spi = SPI(1, baudrate=1000000, polarity=0, phase=0,
          sck=Pin(10), mosi=Pin(11), miso=Pin(8))
cs = Pin(9, Pin.OUT)
sd = sdcard.SDCard(spi, cs)
uos.mount(uos.VfsFat(sd), '/sd')
print("SD card mounted OK")

CSV_FILE = '/sd/sensor_data.csv'
try:
    uos.stat(CSV_FILE)
    print("Existing CSV file found, appending data")
except OSError:
    with open(CSV_FILE, 'w') as f:
        f.write('timestamp,ph,tds_ppm,conductivity_us\n')
    print("New CSV file created with header")

# ── Connect WiFi ───────────────────────────────────────────
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(SSID, PASSWORD)
        timeout = 15
        while not wlan.isconnected() and timeout > 0:
            utime.sleep(1)
            timeout -= 1
    if wlan.isconnected():
        print("WiFi connected! IP:", wlan.ifconfig()[0])
        return True
    else:
        print("WiFi failed — will save to SD only")
        return False

wifi_ok = connect_wifi()

# ── Sync time via NTP ──────────────────────────────────────
rtc = RTC()
if wifi_ok:
    print("Syncing time with NTP...")
    try:
        ntptime.settime()
        print("Time synced!")
    except Exception as e:
        print("NTP sync failed:", e)
        # Fall back to manual time if NTP fails
        rtc.datetime((2026, 4, 29, 0, 0, 0, 0, 0))
else:
    # No WiFi — set time manually
    # Update this line to current date/time before running
    rtc.datetime((2026, 4, 29, 0, 15, 46, 0, 0))

# ── Sensor functions ───────────────────────────────────────
def read_voltage(adc, samples=20):
    total = 0
    for _ in range(samples):
        total += adc.read_u16()
        utime.sleep(0.01)
    avg = total / samples
    return (avg / 65535) * 3.3

def get_ph():
    voltage = read_voltage(ph_adc)
    return round(PH_M * voltage + PH_B, 2)

def get_tds():
    voltage = read_voltage(tds_adc)
    return round(TDS_K * voltage, 1)

def get_conductivity(tds):
    return round(tds * 2, 1)  # µS/cm approximation

def get_timestamp():
    t = utime.localtime()
    months = ['Jan','Feb','Mar','Apr','May','Jun',
              'Jul','Aug','Sep','Oct','Nov','Dec']
    return '{} {} {:02d}:{:02d}'.format(t[2], months[t[1]-1], t[3], t[4])

# ── Main loop ──────────────────────────────────────────────
print("Starting logging. Press Ctrl+C to stop.\n")
reading_number = 1

while True:
    try:
        ph   = get_ph()
        tds  = get_tds()
        cond = get_conductivity(tds)
        ts   = get_timestamp()

        print("Reading #{}".format(reading_number))
        print("  Time:          ", ts)
        print("  pH:            ", ph)
        print("  TDS:           ", tds, "ppm")
        print("  Conductivity:  ", cond, "uS/cm")

        # ── Save to SD card ────────────────────────────────
        try:
            with open(CSV_FILE, 'a') as f:
                f.write('{},{},{},{}\n'.format(ts, ph, tds, cond))
            print("  SD card:        saved OK")
        except Exception as e:
            print("  SD card error: ", e)

        # ── Send to ThingSpeak ─────────────────────────────
        if wifi_ok:
            try:
                url = (THINGSPEAK_URL +
                       "?api_key={}&field1={:.2f}&field2={:.0f}&field3={:.0f}"
                       .format(THINGSPEAK_WRITE_KEY, ph, tds, cond))
                response = urequests.get(url)
                response.close()
                print("  ThingSpeak:     sent OK")
            except Exception as e:
                print("  ThingSpeak error:", e)
        else:
            print("  ThingSpeak:     skipped (no WiFi)")

        print("---------------------------------------")
        reading_number += 1
        utime.sleep(30)   # 30 seconds for test drive

    except KeyboardInterrupt:
        print("\nLogging stopped.")
        print("Total readings:", reading_number - 1)
        print("Data saved to", CSV_FILE)
        break

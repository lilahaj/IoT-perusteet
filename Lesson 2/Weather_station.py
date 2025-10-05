import network
import time
import urequests
import dht
from machine import Pin

ssid = 'Wokwi-GUEST'
password = ''

THINGSPEAK_API_KEY = 'WV8R1X4GRAYCHERZ'
THINGSPEAK_URL = 'https://api.thingspeak.com/update'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Connecting to Wi-Fi...", end="")
while not wlan.isconnected():
    print(".", end="")
    time.sleep(0.5)
print("\nConnected!")
print("IP address:", wlan.ifconfig()[0])

sensor = dht.DHT22(Pin(15))

def send_to_thingspeak(temp, hum):
    if temp is None and hum is None:
        print("No data to send.")
        return

    try:
        # Build form data: field1 = temperature, field2 = humidity
        payload = 'api_key={}'.format(THINGSPEAK_API_KEY)
        if temp is not None:
            payload += '&field1={}'.format(temp)
        if hum is not None:
            payload += '&field2={}'.format(hum)

        response = urequests.post(
            THINGSPEAK_URL,
            data=payload,
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        print("ThingSpeak response:", response.text)
        response.close()
    except Exception as e:
        print("Failed to send data:", e)

# Main loop: read sensor and send data every 15 seconds
while True:
    try:
        sensor.measure()                      # Trigger measurement (waits internally)
        temperature = sensor.temperature()    # °C
        humidity = sensor.humidity()          # %
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        send_to_thingspeak(temperature, humidity)
    except Exception as e:
        print("Error reading sensor or sending data:", e)

    time.sleep(15)  # Free ThingSpeak-kanavalla min 15 s

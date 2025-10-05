import network       # For Wi-Fi connectivity
import time          # For delays and timing
import urequests     # For making HTTP requests
import dht           # For interfacing with DHT sensors
from machine import Pin  # For controlling GPIO pins

ssid = 'Wokwi-GUEST'     # SSID of the Wi-Fi network
password = ''            # Password (empty for open networks like Wokwi-GUEST)

THINGSPEAK_API_KEY = 'WV8R1X4GRAYCHERZ'  # Your ThingSpeak Write API Key
THINGSPEAK_URL = 'https://api.thingspeak.com/update'  # ThingSpeak endpoint

wlan = network.WLAN(network.STA_IF)  # Create a WLAN object in station mode, the device connects to a Wi-Fi network as a client. 
wlan.active(True)                    # Activate the Wi-Fi interface
wlan.connect(ssid, password)         # Connect to the specified Wi-Fi network


print("Connecting to Wi-Fi...", end="")
while not wlan.isconnected():
    print(".", end="")               # Print dots while waiting
    time.sleep(0.5)                  # Wait half a second before retrying

print("\nConnected!")
print("IP address:", wlan.ifconfig()[0])  # Display the assigned IP address

sensor = dht.DHT22(Pin(15))

def send_to_thingspeak(temp, hum):
    # Build payload: field1 = temperature, field2 = humidity
    if temp is None and hum is None:
        print("No data to send.")
        return

    try:
        payload = 'api_key={}'.format(THINGSPEAK_API_KEY)
        if temp is not None:
            payload += '&field1={}'.format(temp)
        if hum is not None:
            payload += '&field2={}'.format(hum)

        # Send HTTP POST request to ThingSpeak with data
        response = urequests.post(
            THINGSPEAK_URL,
            data=payload,
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        print("ThingSpeak response:", response.text)  # Print server response
        response.close()  # Close the connection

    except Exception as e:
        print("Failed to send data:", e)  # Handle any errors



# Main loop: read sensor and send data every 15 seconds

while True:

    try:
        sensor.measure()                      # Trigger sensor measurement
        temperature = sensor.temperature()    # Read temperature in Celsius
        humidity = sensor.humidity()          # Read relative humidity in %
        print("Temperature:", temperature, "°C")   # Display temperature
        print("Humidity:", humidity, "%")          # Display humidity
        send_to_thingspeak(temperature, humidity)  # Send data to ThingSpeak

    except Exception as e:
        print("Error reading sensor or sending data:", e)  # Handle errors

    time.sleep(15)  # Wait 15 seconds before next reading

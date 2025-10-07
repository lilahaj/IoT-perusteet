# Lämpötila ja kosteus ThingSpeakiin

### Tämä ohjelma lukee DHT22-anturin lämpötilan ja kosteuden ja lähettää ne ThingSpeakiin Wi-Fin kautta. Koodi on tarkoitettu Raspberry Pi Pico W -kortille ja MicroPythonille.
*EXTRA! Lisätty ilmankosteus.*  
<img width="1664" height="509" alt="image" src="https://github.com/user-attachments/assets/d5cc0b53-b7ed-4d20-b88c-2eafdab363af" />

### Toiminta
Yhdistyy määriteltyyn Wi-Fi-verkkoon.  
Lukee lämpötilan ja kosteuden DHT22-sensorista.  
Lähettää arvot ThingSpeakiin:  
Field 1: lämpötila (°C)  
Field 2: kosteus (%)  
Toistaa mittauksen ja lähetyksen 15 sekunnin välein.  
Tulostaa arvot ja ThingSpeakin vasteen sarjaporttiin.

### Laitteisto
Raspberry Pi Pico W (Wi-Fi-malli)  
DHT22-anturi kytketty GPIO 15  
VCC → 3.3 V  
GND → GND  
DATA → GPIO 15

### Käyttö
Luo ThingSpeak-tili ja uusi kanava, jossa on kaksi kenttää:  
Field 1: Temperature (°C)  
Field 2: Humidity (%)  
Kopioi oman kanavasi Write API Key ja liitä se koodissa olevan API:n tilalle


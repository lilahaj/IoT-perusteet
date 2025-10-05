# I2C LCD -näyttö – Raspberry Pi Pico / MicroPython

### Tämä ohjelma näyttää tekstin I2C-liitäntäisellä LCD-näytöllä Raspberry Pi Pico -kortilla. Esimerkissä käytetään 20×4-merkkistä näyttöä (4 riviä, 20 merkkiä).

### Toiminta
Tulostaa näytölle tekstin:  
*Hello student!*

### Tarvittavat kirjastot
Lataa ja tallenna Picoon seuraavat tiedostot (samaan hakemistoon ohjelman kanssa):  
[pico_i2c_lcd.py](https://github.com/T-622/RPI-PICO-I2C-LCD/blob/main/pico_i2c_lcd.py)  
[lcd_api.py](https://github.com/dhylands/python_lcd/blob/master/lcd/lcd_api.py)

### Laitteisto
Raspberry Pi Pico
20×4 tai 16×2 I²C LCD

### Liitännät:
VCC → 5 V  
GND → GND  
SDA → GPIO 0  
SCL → GPIO 1

### Käyttö  
Lataa lcd_api.py ja pico_i2c_lcd.py Picoon.  
Tallenna ohjelma  
Suorita ohjelma → LCD-näyttöön ilmestyy “Hello student!”.

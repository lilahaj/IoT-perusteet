# DHT22-lämpötila- ja kosteusmittaus – Raspberry Pi Pico / MicroPython

### Tämä ohjelma lukee lämpötilan ja kosteuden DHT22-sensorista Raspberry Pi Pico -kortilla MicroPythonin avulla.
### Tulokset tulostetaan sarjaporttiin kahden sekunnin välein.
#

### Toiminta
Alustaa DHT22-anturin GPIO 15 -pinniin.  
Mittaa lämpötilan ja kosteuden.  
Tulostaa arvot.  
Toistaa mittauksen 2 sekunnin välein.  
Jos anturin luku epäonnistuu, tulostaa virheilmoituksen.

### Laitteisto
Raspberry Pi Pico  
DHT22-anturi kytketty GPIO 15:    
- VCC → 3.3 V  
- GND → GND  
- DATA → GPIO 15

### Käyttö  
Asenna dht-kirjasto MicroPythonissa (usein sisäänrakennettu).  
Tallenna ohjelma Picoon nimellä esim. dht22.py.  
Avaa sarjaportti (Thonny, PuTTY, tms.) ja suorita ohjelma.  
Näet mittaustulokset 2 s välein.

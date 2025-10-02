# Reaction Timer – Raspberry Pi Pico / MicroPython (lisätty alustus)

### Reaktioaikamittari Raspberry Pi Pico -kortille.
### LED syttyy satunnaisen viiveen jälkeen → paina nappia → ohjelma mittaa ja tulostaa reaktioajan.
### Tuplaklikkaus aloittaa uuden kierroksen ilman ohjelman uudelleenkäynnistystä.
#
### Toiminta
Odottaa satunnaisen ajan 5–10 s.  
Sytyttää LEDin.  
Mittaa ajan LEDin syttymisestä napinpainallukseen.  
Tulostaa reaktioajan.  
Tuplaklikkaa nappia (≤ 500 ms) → alkaa uusi kierros.

### Laitteisto
Raspberry Pi Pico  
LED kytketty GPIO 15 (sarjavastuksen kautta maahan)  
Painonappi kytketty GPIO 14, PULL_DOWN

### Käyttö
Lataa koodi Picoon (MicroPython).  
Kytke LED ja nappi ohjeen mukaisiin GPIO-pinneihin.  
Avaa sarjaportti ja aja ohjelma.  
Paina nappia LEDin syttyessä, tuplaklikkaa aloittaaksesi uuden kierroksen.

### Säätö
Koodin alusta voi muuttaa:  
DBL_WIN – tuplaklikin aikaikkuna (ms), oletus 500

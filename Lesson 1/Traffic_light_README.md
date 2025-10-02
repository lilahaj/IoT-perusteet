# Liikennevalot – Raspberry Pi Pico

*HUOM! Extra toimintoja lisätty!*

### Tässä projektissa on toteutettu liikennevalojen logiikka MicroPythonilla Raspberry Pi Pico -kortille.
### Kytkennöissä käytetään kolmea LEDiä (punainen, keltainen, vihreä), jalankulkijan nappia sekä summeria (valinnainen).

### Toiminta:  
Punainen valo palaa aina oletuksena.  
Kun jalankulkija painaa nappia →
Odotetaan 5 sekuntia (punainen palaa edelleen).  
Syttyy punainen + keltainen yhtä aikaa (1 s).
Vaihdetaan vihreään (5 s).  
Sammutetaan vihreä, syttyy keltainen (2 s).  
Palataan takaisin punaiseen.  
Nappi toimii vain, jos edellinen sykli ei ole kesken.  
Lepotilassa aina punainen valo päällä.



### Laitteisto:  
Raspberry Pi Pico  
LEDit: punainen (Pin 15), keltainen (Pin 14), vihreä (Pin 13)  
Jalankulkijan nappi (Pin 16, PULL_DOWN)  
Summeri (Pin 12, valinnainen)

### Käyttö:  
Lataa koodi Picoon (MicroPython).  
Kytke LEDit, nappi ja summeri ohjeen mukaisiin GPIO-pinneihin.  
Käynnistä ohjelma → punainen valo palaa jatkuvasti.  
Paina nappia → valo-ohjelma käynnistyy.

# LED ja nappi – Raspberry Pi Pico

## Tässä projektissa on toteutettu yksinkertainen nappiohjattu LED Raspberry Pi Pico -kortilla MicroPythonilla.

### Toiminta:

LED on oletuksena sammutettuna.

Kun nappia painetaan, LED syttyy.

Kun nappi vapautetaan, LED sammuu.

### Laitteisto:

Raspberry Pi Pico

LED kytketty GPIO 22:een (sarjavastuksen kautta maahan)

Painonappi kytketty GPIO 13:een ja maahan

Käytetään sisäistä PULL_UP-vastusta → nappi antaa arvon 0, kun sitä painetaan.

### Käyttö:

Lataa koodi Picoon (MicroPython).

Kytke LED pinniin 22 ja painonappi pinniin 13.

Käynnistä ohjelma → LED syttyy ja sammuu napin mukaan.

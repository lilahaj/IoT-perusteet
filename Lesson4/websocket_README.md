# WebSocket-harjoitus – Node.js + HTML-asiakas
### Tämä projekti koostuu Node.js-palvelimesta ja HTML-asiakassivusta, jotka keskustelevat keskenään WebSocket-yhteyden kautta. Harjoituksen tarkoitus on ymmärtää reaaliaikaisen kaksisuuntaisen yhteyden toiminta.

### Toiminta
Node.js käynnistää WebSocket-palvelimen porttiin 8080.  
Selain (HTML-sivu) yhdistää siihen.  
Käyttäjä kirjoittaa viestin tekstikenttään ja painaa Send.  
Palvelin vastaanottaa viestin ja lähettää sen takaisin muodossa: Echo: [viesti].  
Molemmat osapuolet näyttävät viestit omissa lokeissaan.

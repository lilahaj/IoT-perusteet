# Discord Webhook Notifier – Express API

### Tämä on yksinkertainen Node.js (Express) -palvelin, joka lähettää viestejä Discord-kanavalle webhookin kautta. API:n kautta voidaan lähettää JSON-muotoinen viesti, joka välitetään suoraan Discordiin.

### Toiminta  
Vastaanottaa POST-pyynnön osoitteeseen /notify.  
Tarkistaa, että mukana on kenttä message.  
Lähettää sen Discordin webhook-osoitteeseen (DISCORD_WEBHOOK_URL).  
Palauttaa onnistumisesta JSON-vastauksen.

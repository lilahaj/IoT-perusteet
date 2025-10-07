# ThingSpeak Temperature Fetch
### Tämä projekti hakee lämpötiladatan ThingSpeakista ja näyttää sen selaimessa. Datan käsittely tapahtuu JavaScriptin fetch()-funktiolla.

### Toiminta
JavaScript hakee JSON-muotoisen datan ThingSpeak-kanavasta:  
https://api.thingspeak.com/channels/3100740/feeds.json?api_key=50IUUWC8T94XGJS6   
Jokaisesta mittauksesta otetaan:  
Aikaleima (created_at)    
Lämpötila (field1)  
Data muunnetaan taulukoksi ja tulostetaan selaimen #output-elementtiin JSON-muodossa.  
Jos haku epäonnistuu, näytetään virheviesti.

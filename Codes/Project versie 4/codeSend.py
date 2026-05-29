import requests
import random
import time
WEBHOOK_URL = "https://discord.com/api/webhooks/1463215636653277256/vXQWejrTr7essTq7bIp82jEhljXORi3qSfTeI5z__bWpQGKLJBe8rJ-eGSRREdyzRZci"

#wachtwoord=None
def send_discord():
        global wachtwoord
        wachtwoord = str(random.randint(0,9))
  
        data = {"content":wachtwoord}
        print(repr(wachtwoord))
        time.sleep(2)
        requests.post(WEBHOOK_URL, json=data)
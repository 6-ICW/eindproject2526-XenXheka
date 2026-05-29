import RPi.GPIO as GPIO
import time
from foto import stuur_foto
import datetime
import requests
GPIO.setmode(GPIO.BCM)
PIN=4             
GPIO.setup(PIN,GPIO.IN)
url = "http://127.0.0.1:8000/app/set-aanwezig/"
data = {
                    "aanwezig": True,
                    "datum": datetime.datetime.now().isoformat()
                }

def beweging():
    print("Sensor activated")
    time.sleep(.1)
    while True:
        print("WHILE LOOP START")
        time.sleep(2)
        if GPIO.input(PIN):
            print("Movement detected")
            
            stuur_foto()
            r = requests.post(url, json=data, timeout=3)
            print(r.status_code)
        time.sleep(2)
        print("sensor diable")
        break
beweging()
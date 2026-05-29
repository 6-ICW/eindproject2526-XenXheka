import RPi.GPIO as GPIO
import time
import requests
import datetime

from foto import stuur_foto

url = "http://127.0.0.1:8000/app/set-aanwezig/"

GPIO.setmode(GPIO.BCM)
PIN = 25
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def beweging():
    print("Sensor activated")

    try:
        while True:
            if GPIO.input(PIN):
                print("detected")

                print("about to take photo")
                stuur_foto()
                print("photo function done")

                data = {
                    "aanwezig": True,
                    "datum": datetime.datetime.now().isoformat()
                }

                r = requests.post(url, json=data, timeout=3)
                print(r.status_code)

                time.sleep(2)  # anti spam
                break

            time.sleep(0.1)

    except KeyboardInterrupt:
        GPIO.cleanup()
        print("stopped cleanly")

beweging()
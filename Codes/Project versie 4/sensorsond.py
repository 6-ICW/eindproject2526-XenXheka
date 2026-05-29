import RPi.GPIO as GPIO
import time
from stepMotor import rotate
from stepMotor import STEP_PER_90_DEG

TRIG = 21
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def afstand():
    GPIO.output(TRIG, False)
    time.sleep(0.0002)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start_time = time.time()
    timeout = start_time + 0.02
    start = start_time  # ← standaard waarde!
    stop = start_time   # ← standaard waarde!
    while GPIO.input(ECHO) == 0:
        start = time.time()
        if start > timeout:
            return None

    while GPIO.input(ECHO) == 1:
        stop = time.time()
        if stop > timeout:
            return None

    duur = stop - start
    afstand_cm = (duur * 34300) / 2
    return afstand_cm

def start():
    try:
        while True:
            d = afstand()
            if d is None:
                continue  # probeer opnieuw
            
            # trigger rond 8 cm (met marge)
            if 17<=d <= 21:
                    print(d)
                    rotate(STEP_PER_90_DEG, direction =-1)

                    print("🔥 ACTIE! Iets rond 8 cm gedetecteerd")
                    break

            time.sleep(0.3)

    except KeyboardInterrupt:
        GPIO.cleanup()

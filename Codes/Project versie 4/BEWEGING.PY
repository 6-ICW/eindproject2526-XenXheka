import RPi.GPIO as GPIO
import time
PIN=25
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.IN)
print("wachten")
print('klaar om te meten')
try:
    while True:
        if GPIO.input(PIN):
            print("bewging dedected")
        else:
            print("nope")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("gestopt")
    GPIO.cleanup()
    
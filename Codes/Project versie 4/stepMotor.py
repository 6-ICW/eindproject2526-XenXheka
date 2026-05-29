import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
#GPIO instellingen
PINS = [18, 23, 16, 12]
GPIO.setmode(GPIO.BCM)
for pin in PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
    
#--------------------------------
#FULL -STEP sequence: altijd 2 spoelen tegelijk

FULL_STEP = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1]]

STEP_DELAY = 0.003  #verlaag voor sneller, verhoog voor langzamer
STEP_PER_90_DEG = 128  # jouw gemeten waarde

#---------------------------------------
#Draai-functie

def rotate(steps, direction=1):
    if direction == 1:
        seq = FULL_STEP
    else:
        seq = list(reversed(FULL_STEP))             
    
    for _ in range(steps):
        for pattern in seq:
            for pin, value in zip(PINS, pattern):
                GPIO.output(pin, value)
            time.sleep(STEP_DELAY)

#rotate(STEP_PER_90_DEG, direction =-1)
                 
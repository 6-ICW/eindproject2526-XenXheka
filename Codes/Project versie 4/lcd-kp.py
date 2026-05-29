import RPi.GPIO as GPIO
import LCD1602
from kbLib import keypad
import time
from bewegingsensor import beweging
#from codeSend import send_discord
#from codeSend import wachtwoord
from time import sleep
import requests
import random
import time
WEBHOOK_URL = "https://discord.com/api/webhooks/1463215636653277256/vXQWejrTr7essTq7bIp82jEhljXORi3qSfTeI5z__bWpQGKLJBe8rJ-eGSRREdyzRZci"

wachtwoord=None
def send_discord():
        global wachtwoord
        wachtwoord = str(random.randint(0,20))
  
        data = {"content":wachtwoord}
        print(repr(wachtwoord))
        time.sleep(2)
        requests.post(WEBHOOK_URL, json=data)

PINS = [18, 23, 24, 12]
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

STEP_DELAY = 0.003   #verlaag voor sneller, verhoog voor langzamer

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
myPad = keypad(retChar = '#')
LCD1602.init(0x27,1)


    


while True:
    
  
    try:
        while True:
            send_discord()
            
            LCD1602.write(0,0,'Geef code:')
            myString = myPad.readKeypad()        
            LCD1602.write(0,1,myString)
            sleep(2)
            
            
            LCD1602.clear()
            if wachtwoord == myString.strip():
               
                LCD1602.write(0,0,'Code is juist!!!')
                LCD1602.write(0,1,'Trek aan hendel')
                rotate(STEP_PER_90_DEG, direction =1)
                beweging()
                time.sleep(10)
                rotate(STEP_PER_90_DEG, direction =-1)
            else:
                LCD1602.write(0,0, 'Code is fout!!!')
                print(repr(myString))
            sleep(5)
            LCD1602.clear()     
    
    except KeyboardInterrupt:
        sleep(.2)
        LCD1602.clear()
        GPIO.cleanup()



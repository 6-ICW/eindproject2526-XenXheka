import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from sensorsond import start
import LCD1602
import time
from code import code
#from "" import beweging
from bewegingsensor_webcam import Beweging
import codeSend 
from time import sleep
import requests
import random
from mfrc522 import SimpleMFRC522
import time
reader = SimpleMFRC522()
idKaart = 978103413104
from stepMotor import rotate
from stepMotor import STEP_PER_90_DEG
GPIO.setwarnings(False)
from kbLib import keypad
from flushKp import flush_keypad
from wachtopenter import Wacht_Op_Enter
myPad= keypad()
LCD1602.init(0x27,1)
rows=[17,27,22,5]
columns =[6,13,19,26]
keys = [['1','2','3','A'], ['4','5','6','B'],['7','8','9','C'], ['*',"0",'#','D']]
GPIO.setmode(GPIO.BCM)
for r in rows:
    GPIO.setup(r,GPIO.OUT)
    GPIO.output(r,GPIO.LOW)
for c in columns:
    GPIO.setup(c,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def get_key():
    for i, r in enumerate(rows):
        GPIO.output(r,GPIO.HIGH)
        for j,c in enumerate(columns):
            if GPIO.input(c)==1:
                GPIO.output(r,GPIO.LOW)
                return keys[i][j]
            
        GPIO.output(r,GPIO.LOW)
    return None
         

    


   
start_time=time.time()
timeout=5
kaart_ok = False
systeem_status=False
while True:
  k=get_key()
  if k == "#":
    
      
             
        print("Hou je kaart tegen de lezer")
        flush_keypad() 

        while  time.time()-start_time <= timeout:
             try:
                    id,text = reader.read_no_block()
                    if id == idKaart:
                          
                            
                            kaart_ok = True
                            break
                    
             except KeyboardInterrupt:
                 GPIO.cleanup()
                 LCD1602.clear()
        if kaart_ok:
                            LCD1602.write(0,0,'Code is juist!!!')
                            LCD1602.write(0,1,'Trek aan hendel')
                            rotate(STEP_PER_90_DEG, direction =1)
                            time.sleep(1)
                            start()
                            kaart_ok=False
                            LCD1602.clear()
                            
                            start_time=time.time()
        else:
            while True:             
                
                    
                    
                    LCD1602.write(0,0,'Geef code:')
                    #codeSend.send_discord()
                    print("geefcode")
                    myString = myPad.readKeypad()        
                    LCD1602.write(0,1,myString)
                    
                    sleep(2)
                    
                    
                    LCD1602.clear()
                    if code == myString.strip():
                       
                        LCD1602.write(0,0,'Code is juist!!!')
                        LCD1602.write(0,1,'Trek aan hendel')
                        rotate(STEP_PER_90_DEG, direction =1)
                        Beweging()                        
                        kaart_ok=False
                        start_time=time.time()
                        
                        break
                    else:
                        LCD1602.write(0,0, 'Code is fout!!!')
                        print(repr(myString))
                        sleep(5)
                        LCD1602.clear()
                        kaart_ok=False
                 
                 
        
        

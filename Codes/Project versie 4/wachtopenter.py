import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
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
def Wacht_Op_Enter():
    print('HA DRUK OP KNOPPIE OM T STARTEN')
    try:
        while True:
            k=get_key()
            if k == "#":
                print("ok")
            time.sleep(.1)
    except KeyboardInterrupt:
        GPIO.cleanup()

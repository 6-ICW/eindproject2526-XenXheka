import RPi.GPIO as GPIO
from kbLib import keypad
myPad = keypad()
myString = myPad.readKeypad()
print(myString)
GPIO.cleanup()
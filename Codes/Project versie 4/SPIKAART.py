from mfrc522 import SimpleMFRC522
import time
reader = SimpleMFRC522()
idKaart = 742872805023
def draadloos():
    print("Hou je kaart tegen de lezer")

    try:
        id,text = reader.read()
        print("ID", repr(id))
        print("Text", "DIT IS AL GOED BEGEIN")
    finally:
        GPIO.cleanup()
draadloos()
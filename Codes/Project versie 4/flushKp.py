import time
def flush_keypad():
    t0=time.time()
    while time.time() - t0<1:
        try:
            myPad.readKeypad()
        except:
            pass
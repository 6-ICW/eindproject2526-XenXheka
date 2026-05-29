class keypad:
    def __init__(self, rows=[11,13,15,29], columns =[31,33,35,37], keyLabels = [['1','2','3','A'], ['4','5','6','B'],['7','8','9','C'], ['*',0,'#','D']], retChar='#'):
        import RPi.GPIO as GPIO
        self.rows = rows
        self.columns = columns
        self.retChar = retChar
        self.keyLabels = keyLabels
        
        for i in rows:
            GPIO.setup(i, GPIO.OUT)
        for j in columns:
            GPIO.setup(j, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
            
    def readKeypad(self):
        from time import sleep
        import RPi.GPIO as GPIO
        keyStrokes = ''
        noPress =True
        noPressOld=True
        while True:
            noPress = True
            for myRow in [0,1,2,3]:
                for myColumn in [0,1,2,3]:
                    GPIO.output(self.rows[myRow],GPIO.HIGH)
                    butVal = GPIO.input(self.columns[myColumn])
                    GPIO.output(self.rows[myRow], GPIO.LOW)
                    if butVal ==1:
                        myChar =self.keyLabels[myRow][myColumn]
                        if myChar == self.retChar:
                            return keyStrokes
                    noPress = False
                    if butVal ==1 and noPressOld == True and noPress == False:
                        keyStrokes += myChar
                    
            noPresOld = noPress
            sleep(.25)
    

import RPi.GPIO as GPIO
myPad = keypad()
myString = myPad.readKeypad()
print(myString)
GPIO.cleanup()           



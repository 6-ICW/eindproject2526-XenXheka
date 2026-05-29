import cv2
import time
import requests
from foto import stuur_foto
from sendtomessenger import sendBericht
from datetime import datetime
from sensorsond import start

url= "https://api.callmebot.com/facebook/send.php?apikey=Q2MZ41LUZVygfzd5&text=This+is+a+test"
# Instellingen
GEVOELIGHEID = 500        # Hoe lager, hoe gevoeliger (pas aan indien nodig)
COOLDOWN = 10             # Seconden tussen meldingen
CAMERA_INDEX = 0          # 0 = eerste webcam

cap = cv2.VideoCapture(CAMERA_INDEX)
def Beweging():
    if not cap.isOpened():
        print("Kon webcam niet openen!")
        exit()

    print("Webcam gestart, bewegingsdetectie actief...")
    time.sleep(2)  # Wacht even zodat camera opwarmt

    vorig_frame = None
    laatste_melding = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Kon geen frame lezen van webcam!")
            break

        # Verklein en converteer naar grijswaarden voor betere prestaties
        klein = cv2.resize(frame, (640, 480))
        grijs = cv2.cvtColor(klein, cv2.COLOR_BGR2GRAY)
        grijs = cv2.GaussianBlur(grijs, (21, 21), 0)

        if vorig_frame is None:
            vorig_frame = grijs
            continue

        # Bereken verschil tussen frames
        verschil = cv2.absdiff(vorig_frame, grijs)
        drempel = cv2.threshold(verschil, 25, 255, cv2.THRESH_BINARY)[1]
        drempel = cv2.dilate(drempel, None, iterations=2)

        # Zoek contouren (bewegende gebieden)
        contouren, _ = cv2.findContours(drempel.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        beweging_gedetecteerd = False
        for contour in contouren:
            if cv2.contourArea(contour) > GEVOELIGHEID:
                beweging_gedetecteerd = True
                break

        nu = time.time()
        if beweging_gedetecteerd and (nu - laatste_melding) > COOLDOWN:
            print("Beweging gedetecteerd!")
            time.sleep(1)
            start()
            laatste_melding = nu
            requests.get(url)
            cap.release()
            stuur_foto()
            sendBericht()
            response = requests.post('http://localhost:8000/app/set-aanwezig/', json={
                'aanwezig': True,
                'datum': datetime.now().isoformat()
            })
        vorig_frame = grijs
        

        time.sleep(0.1)  # Kleine delay om CPU te sparen
        
    cap.release()

import cv2
import requests
import time


def stuur_foto():
    cam = cv2.VideoCapture(0)
    time.sleep(2)
    ret, frame = cam.read()
    cam.release()
    
    if ret:
        filename = '/home/hekuran/pakket_webcam.jpg'
        cv2.imwrite(filename, frame)
        print("foto opgeslagen")
       
       
            
        
        
        # haal laatste pakje op
        response = requests.get('http://localhost:8000/app/alles/')
        data = response.json()
        leveringen = data['leveringen']
        laatste = max(leveringen, key=lambda x: x['created_at'])
        laatste_pakje_id = laatste['pakje']['id']
       
        # stuur foto naar dat pakje
        with open('/home/hekuran/pakket_webcam.jpg', 'rb') as f:
            response = requests.patch(
                f'http://localhost:8000/app/pakjes/{laatste_pakje_id}/foto/',
                files={'foto': f}
            )
        print(response.status_code)
        foto_url= f"https://skeletal-retouch-eloquent.ngrok-free.dev/app/pakjes/{laatste_pakje_id}/fotosend/"
        url = f"https://api.callmebot.com/facebook/send.php?apikey=Q2MZ41LUZVygfzd5&image={foto_url}"  
        try:
            response = requests.get(url, timeout=5)
            print(response.text)
        except:
            print("ha toch nie")

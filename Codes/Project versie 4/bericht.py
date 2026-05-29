import requests
WEBHOOK_URL = "https://discord.com/api/webhooks/1463202718779969607/ikbvYchEGY5lDk-zX5H0W__IV4RcXGqxwrW0kZdEJCKu3QwPt8qL-XcUKRMP2YmaKN-Z"
def send_discord():
    data = {"content":"Pakket is geleverd"}
    requests.post(WEBHOOK_URL, json=data)
    

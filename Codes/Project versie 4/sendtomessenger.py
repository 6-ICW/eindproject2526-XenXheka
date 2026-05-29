import requests
def sendBericht():
    url = "https://api.callmebot.com/facebook/send.php?apikey=Q2MZ41LUZVygfzd5&text=Pakket geleverd"

    requests.get(url)




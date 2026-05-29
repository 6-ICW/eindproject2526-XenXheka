import requests

response = requests.get('http://localhost:8000/app/alles/')
data = response.json()
laatste = max(data['leveringen'], key=lambda x: x['created_at'])
code = laatste['pakje']['code']
print(f"Code: {code}")
















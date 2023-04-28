import requests

response = requests.post("https://www.example.com", data={"key": "value"})
print(response.text)
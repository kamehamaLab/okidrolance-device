import requests

def UploadServer(key, data):
    response = requests.post("https://www.example.com", data={"key": "value"})
    return(response.text)
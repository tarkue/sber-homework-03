from requests import get
from decouple import config
from time import sleep

url = config("SERVER_URL")

answer = None
while answer == None:
    try:
        request = get(url)
        answer = request.json()
    except Exception: 
        sleep(1)

print(answer)
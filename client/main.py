from requests import get
from os import environ
from time import sleep

url = environ.get("SERVER_URL")

answer = None
while answer == None:
    try:
        request = get(url)
        answer = request.json()
    except Exception: 
        sleep(1)

print(answer)
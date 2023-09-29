import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
code = os.getenv("CODE")
user = os.getenv("USER")
values = {
        "grant_type" : "authorization_code",
        "client_id" : client_id,
        "client_secret" : client_secret,
        "code" : code,
    }

def user_token(values, user):
    link = "https://hh.ru/oauth/token"
    header = {
        "user-agent": user,
    }
    my_req = requests.post(link, headers=header, data=values)
    date = json.loads(my_req.text)
    with open('my_token.json', 'w') as file:
        json.dump(date, file, indent=4)

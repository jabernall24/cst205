import requests
from pprint import pprint
from dotenv import load_dotenv
import os


load_dotenv()
my_key = os.getenv("API_KEY")

url = "https://api.royaleapi.com/player/2GUQQ8JGC/chests"

headers = {
    'auth': my_key
}

response = requests.request("GET", url, headers=headers)

data = response.json()
pprint(data)

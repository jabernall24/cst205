import requests, json
from pprint import pprint

my_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjA1MCwiaWRlbiI6IjQ5MjgyNDgyNTk3OTYwMDg5NyIsIm1kIjp7fSwidHMiOjE1NDMyMTY5Njg3OTV9.okAcprH46D0-MHVmrAatkCifmSAop3i8VK4ZO42sT-w'

url = "https://api.royaleapi.com/player/2GUQQ8JGC/chests"

headers = {
    'auth': my_key
}

response = requests.request("GET", url, headers=headers)

data = response.json()
pprint(data)

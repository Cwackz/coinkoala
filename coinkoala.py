import requests

URL = "https://pastebin.com/raw/4cCGCiyj"

contents = requests.get(URL).text.split('\n')
print(contents)

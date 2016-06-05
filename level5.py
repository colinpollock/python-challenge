import pickle
import requests

response = requests.get('http://www.pythonchallenge.com/pc/def/banner.p')
response.raise_for_status()

data = pickle.loads(response.content)

for line in data:
    for (char, count) in line:
        print(char * count, sep='', end='')
    print()
